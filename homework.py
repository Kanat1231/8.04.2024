#1 Даны два целых числа A и B (A < B). Найти произведение всех целых чисел от A до B включительно.
A = 2
B = 6
container = 1
for i in range(A, B + 1):
    container *= i
print("А-дан, В-ға дейінгі барлық бүтін сандардың көбейтіндісі" ,container ,"ға тең")

#2 Дано целое число N (> 0). Найти сумму 1 + 1/2 + 1/3 + … + 1/N (вещественное число).
N = int(input("нольден жоғары бүтін сан енгізіңіз:"))
sum = 0.0
for i in range(1, N + 1):
    sum += 1.0 / i
print("қатардың қосындысы:",sum)
