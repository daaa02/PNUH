from typing import Text
from konlpy.tag import Komoran
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from connect import Connection

komoran = Komoran()
connect = Connection()

assistant, session_id = connect.assistant_connect('2403128d-0671-4f67-8a12-1c8999bf2256')

class Dictionary():
    def __init__(self):
        
        self.Yes = ['네', '예', '응', '어', '맞아요', '맞아', '그래', '그렇습니다', '맞습니다', '맞어', 
                    '그렇', '있습니다', '있어', '있지']

        self.No = ['아니', '아니오', '아니요', '안', '아뇨', '아닌', '아닙니다', '아냐', '아닐', '별로', 
                   '글쎄', '그다지', '딱히', '없습니다', '없어', '없네', '없는', '없다', '없고', '없음', '없으예', '없소']
        
        self.idk = ["모르", "몰라", "모름", "모릅", "몰라요", "모릅니다", "모르겠어요", "기억이 안", "가물가물"]
        
        self.Number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']

        self.Number_Word = ['영', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구', '십', '십일']

        self.acc_1 = ['교통사고', '교통 사고', '차 사고', '차사고', '교통', '자동차', '차']

        self.acc_2 = ['넘어짐', '넘어', '넘어졌', '넘어지고', '넘어져', '넘어진']

        self.acc_3 = ['떨어짐', '추락', '떨어', '떨어졌', '떨어져', '덜어', '떨어지']

        self.acc_4 = ['구름', '굴렀', '굴러', '굴러', '굴렀', '구르게', '구르면서']

        self.acc_5 = ['폭행', '맞았', '맞아서', '몸싸움', '때리', '때려', '맞으', '맞은', '맞는', '맞고', '맞아']

        

class NLP():
    def __init__(self):
        self.komoran = Komoran()
        self.temp = {}
        
        
    def nlp_answer(self, user_said, dic):
        answer = ''
        for i in range(len(dic.Yes)):
            if dic.Yes[i] in user_said:
                answer = '네'
        for j in range(len(dic.No)):
            if dic.No[j] in user_said:
                answer = '아니오'
        for k in range(len(dic.idk)):
            if dic.idk[k] in user_said:
                answer = '모름'
        # print(answer)
        return answer    
    
    
    def nlp_number(self, user_said, dic):
        number = -1
        ko = -1
        nb = -1
        for i, j in enumerate(dic.Number_Word):
            x = user_said.find(j)
            if x != -1:
                ko = i
        for i, j in enumerate(dic.Number):
            x = user_said.find(j)
            if x != -1:
                nb = i
        number = max(ko, nb)
        return number


    def nlp_accident(self, user_said, dic):
        answer = ''
        for i in range(len(dic.acc_1)):
            if dic.acc_1[i] in user_said:
                answer = '교통사고'
        for j in range(len(dic.acc_2)):
            if dic.acc_2[j] in user_said:
                answer = '넘어짐'
        for k in range(len(dic.acc_3)):
            if dic.acc_3[k] in user_said:
                answer = '떨어짐'
        for m in range(len(dic.acc_4)):
            if dic.acc_4[k] in user_said:
                answer = '구름'
        for n in range(len(dic.acc_5)):
            if dic.acc_5[k] in user_said:
                answer = '폭행'
        # print(answer)
        return answer

    
    
    def nlp_medicine(self, sentence):
        answer = []
        clean = []        
        stopwords = ['이랑']
        nouns = komoran.nouns(sentence) 
        for i in range(len(nouns)):
            if nouns[i] not in stopwords:
                clean.append(nouns[i] + "약")
                # print(f"clean = {clean}")   # 나 진짜 천잰가                
            answer = clean         
        # print(answer)
        return answer

    def nlp_komoran(self, sentence):
        answer = []
        clean = []
        stopwods = ['이랑']
        nouns = komoran.nouns(sentence)
        for i in range(len(nouns)):
            if nouns[i] not in stopwods:
                clean.append(nouns[i])
            answer = clean
        # print(answer)
        return answer 
    
    
    def watson(self, user_said, list_name):
        """
        * user_said 으로부터 intents 추출하고, 리스트에 저장
            : Watson Assistant -> Dialog -> Intents 
        """
        response = assistant.message(
                    assistant_id = '2403128d-0671-4f67-8a12-1c8999bf2256',
                    session_id = session_id,
                    input = {
                        'message_type': 'text',
                        'text': user_said
                    }
                ).get_result()['output']
        
        # list_name = []
        [list_name.append(response["intents"][i]["intent"]) for i in range(len(response["intents"])) 
        if response["intents"][i]["confidence"] > 0.5]
    
        return response, list_name


    def watson_position(self, user_said, list_name):
        """
        * 통증 부위 질문에서만 사용
        """
        response = assistant.message(
            assistant_id = '2403128d-0671-4f67-8a12-1c8999bf2256',
            session_id = session_id,
            input = {
                'message_type': 'text',
                'text': user_said
            }
        ).get_result()['output']
                                        
        for i in range(len(response["entities"])):
            if response["entities"][i]["entity"] == "신체부위":
                list_name.append(response["entities"][i]["value"])
                        
        return response, list_name


    def watson_time(self, user_said, list_name):
        """
        * 통증 발생 시기 질문에서만 사용
        """
        response = assistant.message(
            assistant_id = '2403128d-0671-4f67-8a12-1c8999bf2256',
            session_id = session_id,
            input = {
                'message_type': 'text',
                'text': user_said
            }
        ).get_result()['output']
                                        
        for i in range(len(response["entities"])):
            if response["entities"][i]["entity"] == "통증시기":
                for j in range(len(response["entities"][i]["value"])):
                    if response["entities"][i]["value"][j] == '년':
                        list_name.append(response["entities"][i]["value"])
                    elif response["entities"][i]["value"][j] == '월':
                        list_name.append(response["entities"][i]["value"])
                    elif response["entities"][i]["value"][j] == '일':
                        list_name.append(response["entities"][i]["value"])
                        
        return response, list_name
    
    
