team1_num = 5
string_with_team1_num = "В команде Мастера кода участников: %d !" % team1_num
print(string_with_team1_num)

team1_num = 5
team2_num = 6
string_with_both_teams = "Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num)
print(string_with_both_teams)

score_2 = 42
string_with_score_2 = "Команда Волшебники данных решила задач: {} !".format(score_2)
print(string_with_score_2)

team2_time = 18015.2
string_with_team2_time = "Волшебники данных решили задачи за {:.1f} с !".format(team2_time)
print(string_with_team2_time)

score_1 = 40
score_2 = 42
string_with_scores = f"Команды решили {score_1} и {score_2} задач."
print(string_with_scores)

challenge_result = 'Победа команды Мастера кода!'
string_with_challenge_result = f"Результат битвы: {challenge_result}"
print(string_with_challenge_result)

tasks_total = 82
time_avg = 350.4
string_with_tasks_and_time = f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg:.1f} секунды на задачу!."
print(string_with_tasks_and_time)