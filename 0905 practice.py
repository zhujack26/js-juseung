import socket
import time
import math



def play(conn, gameData):
    angle = 0.0
    power = 0.0

    ##############################
    # 이 위는 일타싸피와 통신하여 데이터를 주고 받기 위해 작성된 부분이므로 수정하면 안됩니다.
    #
    # 모든 수신값은 gameData에 들어갑니다.
    #   - gameData.order: 1인 경우 선공, 2인 경우 후공을 의미
    #   - gameData.balls[][]: 일타싸피 정보를 수신해서 각 공의 좌표를 배열로 저장
    #     예) gameData.balls[0][0]: 흰 공의 X좌표
    #         gameData.balls[0][1]: 흰 공의 Y좌표
    #         gameData.balls[1][0]: 1번 공의 X좌표
    #         gameData.balls[4][0]: 4번 공의 X좌표
    #         gameData.balls[5][0]: 마지막 번호(8번) 공의 X좌표

    # 여기서부터 코드를 작성하세요.
    # 아래에 있는 것은 샘플로 작성된 코드이므로 자유롭게 변경할 수 있습니다.

    # whiteBall_x, whiteBall_y: 흰 공의 X, Y좌표를 나타내기 위해 사용한 변수
    whiteBall_x = gameData.balls[0][0]
    whiteBall_y = gameData.balls[0][1]

    # targetBall_x, targetBall_y: 목적구의 X, Y좌표를 나타내기 위해 사용한 변수
    targetBall_x = gameData.balls[1][0]
    targetBall_y = gameData.balls[1][1]



    # width, height: 목적구와 흰 공의 X좌표 간의 거리, Y좌표 간의 거리
    width = abs(targetBall_x - whiteBall_x)
    height = abs(targetBall_y - whiteBall_y)

    # 목적구가 흰 공의 우측 일직선상에 위치 했을 때
    if targetBall_x > whiteBall_x and targetBall_y > whiteBall_y:
        radian = math.atan(width / height)
        angle = 180 / math.pi * radian

        if 0 <= four_ball_x <= 254 and 0 <= four_ball_y <= 127:
            if four_ball_x < whiteBall_x:
                radian = math.atan(height / width)
                angle = (180 / math.pi * radian) +90

        elif targetBall_y < whiteBall_y and targetBall_x > whiteBall_x:
            radian = math.atan(height / width)
            angle = (180 / math.pi * radian) + 270

            180

    # distance: 두 점(좌표) 사이의 거리를 계산
    distance = math.sqrt(width  2 + height  2)

    # power: 거리 distance에 따른 힘의 세기를 계산
    power = distance * 0.48

       # 여기서부터 코드를 작성하세요.
           # 아래에 있는 것은 샘플로 작성된 코드이므로 자유롭게 변경할 수 있습니다.

           # whiteBall_x, whiteBall_y: 흰 공의 X, Y좌표를 나타내기 위해 사용한 변수
           whiteBall_x = gameData.balls[0][0]
           whiteBall_y = gameData.balls[0][1]

           # targetBall_x, targetBall_y: 목적구의 X, Y좌표를 나타내기 위해 사용한 변수
           targetBall_x = gameData.balls[1][0]
           targetBall_y = gameData.balls[1][1]
           targetBall_x3 = gameData.balls[3][0]
           targetBall_y3 = gameData.balls[3][1]

           # width, height: 목적구와 흰 공의 X좌표 간의 거리, Y좌표 간의 거리
           width = abs(targetBall_x - whiteBall_x)
           height = abs(targetBall_y - whiteBall_y)
           width3 = abs(targetBall_x3 - whiteBall_x)
           height3 = abs(targetBall_y3 - whiteBall_y)

           # radian: width와 height를 두 변으로 하는 직각삼각형의 각도를 구한 결과
           #   - 1radian = 180 / PI (도)
           #   - 1도 = PI / 180 (radian)
           # angle: 아크탄젠트로 얻은 각도 radian을 degree로 환산한 결과
           if targetBall_y - whiteBall_y > 0:  # 5단계에서 height 같은 것 방지 : ZeroDivisionError
               radian = math.atan(width / height)
               angle = 180 / math.pi * radian
               radian3 = math.atan(width3 / height3)

           if targetBall_x - whiteBall_x > targetBall_x3 - whiteBall_x:  # 4단계에서 첫 시작 위치 기준 1사분면에 위치한 1번 공 먼저
               # 목적구가 흰 공을 중심으로 2사분면에 위치했을 때 각도를 재계산
               if whiteBall_x < targetBall_x and whiteBall_y > targetBall_y:
                   radian = math.atan(height / width)
                   angle = (180 / math.pi * radian) + 90

               # 목적구가 흰 공을 중심으로 3사분면에 위치했을 때 각도를 재계산
               if whiteBall_x > targetBall_x and whiteBall_y > targetBall_y:
                   radian = math.atan(width / height)
                   angle = (180 / math.pi * radian) + 180
           else:  # 3번 공
               if whiteBall_x > targetBall_x3 and whiteBall_y < targetBall_y3:
                   radian3 = math.atan(height3 / width3)
                   angle = (180 + math.pi * radian3) + 90

           # distance: 두 점(좌표) 사이의 거리를 계산
           distance = math.sqrt(width**2 + height**2)

           # power: 거리 distance에 따른 힘의 세기를 계산
           power = distance * 0.45