import random  # 카드 숫자, 무늬, 폭탄 여부를 무작위로 만들기 위해 random 모듈 사용
import time    # 게임 시작과 끝 사이 시간 측정을 위해 time 모듈 사용

# 게임 제목 및 규칙을 출력하여 사용자에게 게임 개요를 알려줌
print("♠️ 원카드 게임 ♦️")
print("🔥 너 vs 컴퓨터 🔥")
print("📔 게임 규칙 안내 📔")
print("1. 플레이어와 컴퓨터는 랜덤 카드 5장씩 받습니다.")
print("2. 테이블에는 랜덤 카드 1장이 놓입니다.")
print("3. 플레이어는 숫자나 무늬가 테이블 카드와 같으면 카드를 낼 수 있습니다.")
print("4. 낼 카드가 없으면 'q'를 눌러 카드 1장을 받습니다. (만약 카드를 잘못 내거나 q를 제대로 누르지 않았다면 다음 차례로 넘어감)")
print("5. 폭탄 카드는 20% 확률로 등장하며, 내면 상대가 카드 2장을 받습니다.")
print("6. 카드가 먼저 사라지는쪽이 승리함")

# 사용자에게 이름을 입력받아 게임에 사용할 이름으로 저장
player_name = input("당신의 이름을 입력하세요: ")  

# Enter 키 입력 전까지 대기 → 사용자 준비 완료 후 게임 시작
input("게임을 시작하려면 Enter를 누르세요 🔽")

# 사용할 카드 무늬 리스트 생성 (♠️, ♥️, ♦️, ♣️ 네 종류)
shapes = ['♠️', '♥️', '♦️', '♣️']  

# 플레이어와 봇의 카드 목록을 저장할 빈 리스트 생성
player_hand = []    
bot_hand = []       

# 플레이어에게 카드 5장을 랜덤으로 나눠줌
for _ in range(5):  
    card_num = random.randint(1, 12)  # 1~12 사이의 숫자 카드 생성
    card_shape = random.choice(shapes)  # 무늬 중 하나 무작위 선택
    card_bomb = 'bomb' if random.random() <= 0.2 else ''  # 20% 확률로 폭탄 지정 
    player_hand.append((card_num, card_shape, card_bomb))  # 생성된 카드를 튜플로 저장 후 플레이어 패에 추가

# 봇에게도 똑같이 카드 5장을 랜덤으로 생성하여 줌
for _ in range(5):
    card_num = random.randint(1, 12)
    card_shape = random.choice(shapes)
    card_bomb = 'bomb' if random.random() <= 0.2 else ''
    bot_hand.append((card_num, card_shape, card_bomb))

# 테이블에 놓을 첫 번째 카드 생성
table_num = random.randint(1, 12)
table_shape = random.choice(shapes)
table_bomb = 'bomb' if random.random() <= 0.2 else ''
table_card = (table_num, table_shape, table_bomb)  # 테이블 카드도 튜플 형태로 저장

# 게임 시작 시점을 기록해 나중에 총 플레이 시간 계산에 사용
start_time = time.time()  

# 게임이 끝났는지 여부를 저장할 변수 (기본은 False)
game_over = False  

# 게임이 끝날 때까지 반복
while not game_over:

    # 현재 테이블 위 카드 출력 (폭탄 표시 포함)
    print("\n테이블 카드:", table_card[0], table_card[1], "💣" if table_card[2] == 'bomb' else "") 
    
    # 플레이어의 현재 카드들을 번호와 함께 출력
    print(f"{player_name}님의 카드:")
    idx = 0
    while idx < len(player_hand):  # 손에 있는 카드 수만큼 반복
        card = player_hand[idx]  # 인덱스에 해당하는 카드 가져옴
        bomb_mark = "💣" if card[2] == 'bomb' else ""  # 폭탄 여부 확인 후 표시
        print(idx, ".", card[0], card[1], bomb_mark)  # 카드 번호, 숫자, 무늬, 폭탄 여부 출력
        idx = idx + 1  # 다음 카드로 이동

    # 사용자에게 카드 번호 또는 'q'를 입력받음
    choice = input("낼 카드 번호를 입력하거나 'q'를 눌러 카드 받기: ")

    # 사용자가 'q'를 눌렀을 경우
    if choice == "q":
        # 카드 한 장 생성해서 손패에 추가
        card_num = random.randint(1, 12)
        card_shape = random.choice(shapes)
        card_bomb = 'bomb' if random.random() <= 0.2 else ''
        player_hand.append((card_num, card_shape, card_bomb))
        print("카드 받음:", card_num, card_shape, "💣" if card_bomb == 'bomb' else "")
    else:
        try: # 중첩 if문
            card_index = int(choice)  # 입력값을 정수로 변환
            if 0 <= card_index < len(player_hand):  # 인덱스 번호 0 ~ 낼 수 있는 인덱스
                selected_card = player_hand[card_index]  # 해당 카드 선택
                # 숫자 또는 무늬가 테이블 카드와 같을 경우 낼 수 있음
                if selected_card[0] == table_card[0] or selected_card[1] == table_card[1]:
                    table_card = selected_card  # 테이블 카드 업데이트
                    player_hand.pop(card_index)  # 낸 카드는 손에서 제거
                    print("낸 카드:", selected_card[0], selected_card[1], "💣" if selected_card[2] == 'bomb' else "")
                    if selected_card[2] == 'bomb':  # 낸 카드가 폭탄이면
                        for _ in range(2):  # 봇이 카드 2장 받음
                            card_num = random.randint(1, 12)
                            card_shape = random.choice(shapes)
                            card_bomb = 'bomb' if random.random() < 0.2 else ''
                            bot_hand.append((card_num, card_shape, card_bomb))
                        print("💥 봇이 카드 2장을 받았습니다!")
                else:
                    print("❌ 이 카드는 낼 수 없습니다.")  # 규칙 위반
            else:
                print("❌ 이 카드는 낼 수 없습니다.")  # 인덱스 범위 초과
        except:
            print("❌ 이 카드는 낼 수 없습니다.")  # 숫자 변환 실패 등 예외 처리

    # 플레이어의 손에 카드가 없으면 승리
    if len(player_hand) == 0:
        print(f"\n🎉 {player_name}님 승리! 축하합니다! 🎉")
        game_over = True
        break  # 게임 종료

    # 컴퓨터 차례 안내
    print("\n🤖 봇 차례...")
    time.sleep(1)  # 봇이 생각하는 척 1초 기다림

    # 봇이 낼 수 있는 카드가 있는지 확인
    bot_played = False  # 봇이 카드를 냈는지 여부 (False 아직 내지 않음)
    i = 0
    while i < len(bot_hand):  # 봇의 카드 하나씩 확인
        card = bot_hand[i]
        if card[0] == table_card[0] or card[1] == table_card[1]:  # 낼 수 있는 카드 발견
            table_card = card  # 테이블 카드 교체
            bot_hand.pop(i)  # 낸 카드 제거
            print("봇이 낸 카드:", card[0], card[1], "💣" if card[2] == 'bomb' else "")
            bot_played = True # 카드를 냈음을 표시 (True)
            if card[2] == 'bomb':  # 폭탄 카드일 경우
                for _ in range(2):  # 플레이어가 카드 2장 받음
                    card_num = random.randint(1, 12)
                    card_shape = random.choice(shapes)
                    card_bomb = 'bomb' if random.random() <= 0.2 else ''
                    player_hand.append((card_num, card_shape, card_bomb))
                print("💥 당신이 카드 2장을 받았습니다!")
            break  # 봇은 카드 1장만 내고 종료
        else:
            i = i + 1  # 다음 카드 확인

    # 낼 수 있는 카드가 없었을 경우 카드 1장 받음
    if not bot_played:
        card_num = random.randint(1, 12)
        card_shape = random.choice(shapes)
        card_bomb = 'bomb' if random.random() <= 0.2 else ''
        bot_hand.append((card_num, card_shape, card_bomb))
        print("봇이 카드 1장을 받았습니다.")

    # 봇이 카드 다 냈으면 봇 승리
    if len(bot_hand) == 0:
        print("\n😵 봇 승리! 다음에 다시 도전하세요!")
        game_over = True
        break  # 게임 종료

# 게임 끝난 후 경과 시간 계산
end_time = time.time()
final_time = end_time - start_time  # 전체 플레이 시간 계산
print(f"⏱️ 총 플레이 시간: {final_time:.2f}초")

# 종료 메시지 출력 및 사용자 확인 대기
input("게임 종료! Enter 키를 눌러 종료하세요.")
