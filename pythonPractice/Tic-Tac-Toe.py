import tensorflow as tf
import numpy as np
import csv
import sklearn as sk
import copy
import sys
from sklearn.model_selection import train_test_split

# tf.set_random_seed(777)# 항상 동일한 랜덤 값을 가지게
print(tf.__version__)

matrix = []  # 데이터가 들어갈 matrix

f = open('tic-tac-toe.csv', 'r', encoding='utf-8')
data = csv.reader(f)
for row in data:
    matrix.append(row)  # 데이터행렬삽입
f.close()

dataIn = np.array(matrix)
dataIn = dataIn.astype('float32')  # 문자열 행렬을 형변환

X = dataIn[:, 0:9]  # 10열중 1~9열을 잘라서 X에 넣기
y = dataIn[:, 9:10]  # 10열 (정답)을 잘라서 y에 넣기

# 학습 7 테스트 3비율로 나누기
# train_test_split 를 사용
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
print(X_train.shape)
print(X_test.shape)

print(y_train.shape)

print(y_test.shape)

# placeholder로 자리유지
# 생성될 때 값을 가지지 않고 자리유지하는 개념
X = tf.placeholder(tf.float32, [None, 9], name='x-input')
Y = tf.placeholder(tf.float32, [None, 1], name='y-input')

# 가중치와 바이어스를 변수로 선언
W = tf.Variable(tf.random_normal([9, 1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

# 활성화 함수로 시그모이드사용
y_out = tf.sigmoid(tf.matmul(X, W) + b)
# 손실함수로 '교차 엔트로피 오차' 사용
cost = -tf.reduce_mean(Y * tf.log(y_out) + (1 - Y) * tf.log(1 - y_out))
# 경사하강법으로 최소값 찾기
# 이미 구현된 경사하강법 라이브러리 사용
# 손실함수의 최소값을 구한다.
train = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(cost)

# 예측 결과, 정확도 계산
# 시그모이드의 결과는 0과 1이사이의 값 이므로 0.5가 넘으면 1로본다.
# 실제 y가 1일 때 예측값 1이면 cost감소 예측값 0이면 cost증가
predicted = tf.cast(y_out > 0.5, dtype=tf.float32)
# 예측한 값을 정답과 비교 후 평균낸다.
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, Y), dtype=tf.float32))
# accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())  # 초기화 후 세션에 전

    for step in range(3001):  # 반복횟수 간격은 step100으로 설정
        sess.run(train, feed_dict={X: X_train, Y: y_train})

        if step % 100 == 0:
            print(step, sess.run(cost, feed_dict={X: X_train, Y: y_train}), sess.run(W))

    # 정확도
    h, c, a = sess.run([y_out, predicted, accuracy], feed_dict={X: X_train, Y: y_train})
    ta = sess.run(accuracy, feed_dict={X: X_test, Y: y_test})
    # print("\y_out: ", h, "\nCorrect: ", c, "\nAccuracy: ", a)
    print("\nTrain Accuracy: ", a, "\nTest Accuracy: ", ta)
    # print(sess.run(accuracy, feed_dict={X: X_test, Y: y_test}))
    X = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0], dtype='f')
    X = X.reshape(1, 9)

    for i in range(1, 6):
        a = input('숫자를 입력하세요: ')
        if a == '1':
            X[:, 0:1] = 1
        elif a == '2':
            X[:, 1:2] = 1
        elif a == '3':
            X[:, 2:3] = 1
        elif a == '4':
            X[:, 3:4] = 1
        elif a == '5':
            X[:, 4:5] = 1
        elif a == '6':
            X[:, 5:6] = 1
        elif a == '7':
            X[:, 6:7] = 1
        elif a == '8':
            X[:, 7:8] = 1
        else:
            X[:, 8:9] = 1
        # print(X.reshape(3, 3))

        y = tf.sigmoid(tf.matmul(X, W) + b)
        result = sess.run(y)
        print(result)

        Xzero = copy.deepcopy(X)  # X의 배열 복사

        zero = np.flatnonzero(Xzero == 0)  # X 중에 0인 인덱스 찾기
        r = np.array([], dtype=np.float32)

        for k in range(0, len(zero)):
            Xzero[:, zero[k]:zero[k] + 1] = -1  # 0인 인덱스에 -1 넣기
            yzero = tf.sigmoid(tf.matmul(Xzero, W) + b)
            yapnd = sess.run(yzero)
            print(Xzero)
            # print(yapnd)
            yapnd_c = copy.deepcopy(yapnd)
            wmax = np.max(yapnd_c)
            # print(yapnd_c)
            # print(wmax)

            r = np.append(r, float(wmax))
            print(r)
            # 배열에 추가하고 다시 0으로
            Xzero[:, zero[k]:zero[k] + 1] = 0
        print(r)
        rmin = np.argmin(r)  # 가장 작은 값 인덱스찾기
        X[:, zero[rmin]:zero[rmin] + 1] = -1
        print(X.reshape(3, 3))

        Xshape = X.reshape(3, 3)

        for i in range(1, 4):
            if np.sum(Xshape[:, i - 1:i]) == 3:
                print('승리했습니다.')
                sys.exit()
            if np.sum(Xshape[i - 1:i, :]) == 3:
                print('승리했습니다.')
                sys.exit()
            if np.sum(Xshape[i - 1:i, :]) == -3:
                print('패배했습니다.')
                sys.exit()
            if np.sum(Xshape[i - 1:i, :]) == -3:
                print('패배했습니다.')
                sys.exit()
        diagonal = np.trace(Xshape)  # 대각
        Xdiagonal = np.sum(np.matrix.diagonal(np.fliplr(Xshape)))  # 반대 대각
        if diagonal == 3:
            print('승리했습니다.')
            sys.exit()
        if diagonal == -3:
            print('패배했습니다.')
            sys.exit()
        if Xdiagonal == 3:
            print('승리했습니다.')
            sys.exit()
        if Xdiagonal == -3:
            print('패배했습니다.')
            sys.exit()
# with 구문 다 돌면 세션 자동 종료