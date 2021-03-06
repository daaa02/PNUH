question_list = \
    {
        'Greeting': ["안녕하세요. 저는 외래 초진 환자의 기록 작성을 도와주는 로봇입니다. \
                     제가 하는 질문에 한 분만 또박또박 대답하시면 됩니다.\
                     문진을 시작해도 되겠습니까? '네'라고 대답하시면 시작하겠습니다."],
        
        # 1. 통증 위치/강도/양상
        'Symptoms': ["아픈 곳이 있습니까? '네', '아니오'로 대답해 주세요.",
                     
                     "아프지 않으시다면 여기로 오시게 된 가장 불편한 증상은 무엇입니까?",                     
                     "또 다른 증상이 있습니까? 있으시면 해당 증상을 하나씩 말씀해주시고 없으시면 '없다'라고 말씀해주세요.",
                     
                     "가장 아픈 신체 부위 하나만 말씀해 주세요.",
                     "다음 아픈 부위는 어디입니까? 있으시면 한 부위만 추가로 말씀해주시고 없으시면 “없다”라고 말씀해 주세요",
                     
                     "이제 얼마나 아픈지 물어보겠습니다. 가장 아픈 곳은 ",
                     "그 다음으로 아픈 곳에 대해 물어보겠습니다. 그 다음으로 아픈 부위는 ",     # 대답한 신체 부위 개수만큼 반복
                     
                     " 인데, 그 아픈 정도가 10점 만점에 몇 점 정도 되는가요? '3점', '7점'과 같이 대답해 주세요.",
                     "이 부위가 어떻게 아픈지 간단히 말로 표현해 주세요. 예를 들면 '욱신거린다', '따갑다' 등과 같이 대답해 주세요.",
                     "아픈 것 이외에 다른 증상이 있습니까? 있으시면 해당 증상을 하나씩 말씀해 주시고, 없으시면 '없다' 라고 말씀해 주세요."],
        
        # 2. 발생 시기
        'Occurrence': ["말씀하셨던 증상은 언제부터 발생했습니까? 년/월/일을 구체적으로 말씀해 주세요. 잘 모르시겠다면 '잘 모르겠다' 라고 대답해 주세요.",
                       "정확한 날짜를 모르시겠다면 대략적으로 얼마 전에 발생하셨습니까? 며칠 전, 한 달 전 등으로 말씀해 주세요."],
        
        # 3. 발생 원인
        'Cause': ["말씀하셨던 증상이 발생한 원인이 넘어지거나 다치는 등의 사고와 관련이 있습니까? '네', '아니오'로 대답해 주세요.",  # '아니오' 면 패스
                  "어떤 사고 입니까? '넘어졌다', '교통사고' 등과 같이 대답해 주세요.",
                  "차나 오토바이에 직접 부딪히셨습니까? '네', '아니오' 로 대답해 주세요.", 
                  "사고 때 차 안에 계셨습니까? '네', '아니오'로 대답해 주세요.",
                  "넘어진 장소는 어디입니까? 화장실, 작업장 등으로 대답해 주세요.",
                  "얼마나 높은 장소에서 떨어지셨습니까? '일 미터' 등 대략적으로 말씀해 주세요.",
                  "몇 계단 정도 굴렀습니까? '열 계단' 등 대략적으로 말씀해 주세요.",
                  "이러한 사고가 일하던 중에 발생하여 산재보험으로 처리하실 예정입니까? '네', '아니오', '잘 모르겠다' 중에서 대답해 주세요."],
        
        # 4. 검사 이력
        'CheckUp': ["이러한 증상들로 다른 병원에서 검사를 받으셨습니까? '네',' 아니오'로 대답해 주세요.",
                    "어떤 검사를 받으셨는지 아십니까? '네', '아니오'로 대답해 주세요.",
                    "어떤 검사를 받으셨는지 아신다면 검사 종류를 모두 대답해주세요. 예를 들어 '엑스레이', 'CT' 등으로 대답해 주세요."],
        
        # 5. 치료 여부
        'Treatment': ["이러한 증상들로 다른 병원에서 치료를 받으셨습니까? '네, '아니오'로 대답해 주세요.",
                      "어떤 치료를 받으셨는지 아십니까? '네', '아니오'로 대답해 주세요.",
                      "어떤 치료를 받으셨는지 아신다면 치료 종류를 모두 대답해주세요. 예를 들어 '약물치료', '물리치료' 등으로 대답해 주세요."],
        
        #6. 복용중인 약
        'Medicine': ["현재 드시고 있는 약이 있으십니까? '네', '아니오'로 대답해 주세요.",
                     "현재 먹는 약 중에 지혈을 억제하는 약이 있습니까? '네', '아니오', '잘 모르겠다' 로 대답해 주세요.",
                     "그 외에 드시고 있는 약을 말씀해 주세요. 예를 들어 '혈압약', '당뇨약' 등으로 대답해 주세요. 없으시면 '없다'라고 말씀해 주세요."],
        
        # 7. 과거력
        'Anamnesis': ["현재 약은 먹고 있지 않지만 예전에 앓으셨던 병이 있습니까? '결핵', '간염' 등으로 말씀해 주세요. 없으시면 '없다'라고 말씀해 주세요."],
        
        # 8. 수술이력
        'Surgery': ["예전에 수술이나 시술을 받으신 적이 있습니까? '네', '아니오'로 대답해 주세요.",
                    "가장 최근에 수술이나 시술을 받은 신체 부위를 말씀해 주세요.",
                    "그 다음에 수술을 받은 부위는 어디입니까? 있으시면 한 부위만 추가로 말씀해 주시고, 없으시면 '없다'라고 말씀해 주세요."]
    }    
