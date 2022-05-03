n = int(input())
k = int(input())

card = []
dp = [0] * n  #각 자리수를 썼냐 안썼나 판별하기 위한 리스트

result = 0 #결합된 숫자들을 모아둔 변수

for _ in range(n):
    card.append(int(input()))

string = '' #각 자리의 숫자를 받아와 합쳐주는 역할
result = set() #결합된 숫자들의 중복된 값을 지워주는 역할


def select(cnt):
    global string # 지역변수를 광역변수로 해줘야 함수 바깥에 있는 string 함수와 연동될 수 있음

    if cnt == k: #카운트와 입력받은 k 값이 같게 된다면 조합된 string값을 결괏괎에 넣어주기 위함
        result.add(string)
        return

    for i in range(n): 
        if dp[i] == 0: # 아직 사용이 안된 자리수라면
            dp[i] = 1 # 사용이 되었다고 알려주기 위해 1을 넣어주고

            tmp = str(card[i]) #그 자리수의 card값을 tmp라는 변수에 넣어준 후
            string += tmp # string 기존에 받았던 값과 합쳐준다

            select(cnt + 1)   #cnt+1을 해준다

            dp[i] = 0 # 사용되었던 1을 다시 0 으로 바꿔주어서
            string = string[:-len(tmp)] # 기존에 받았던 값이 있던 string의 위에서 1->0으로 바꾼 자릿수의 값만 제거 후 받아주는 역할을 한다.


select(0)
print(len(result))