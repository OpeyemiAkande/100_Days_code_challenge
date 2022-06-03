# student_scores = {'Harry': 81, 'Ron': 78, 'Hermione': 99, 'Draco': 74, 'Neville':62}

# student_grades = {}

# for student in student_scores:
#     if student_scores[student] > 90:
#         student_grades[student] = 'Outstanding'
#     elif student_scores[student] > 80 and student_scores[student]  <=90:
#         student_grades[student] = 'Exceeded Expectation'
#     elif student_scores[student] > 70 and student_scores[student]  <=80:
#         student_grades[student] = 'Acceptable'
#     elif student_scores[student] <= 70:
#         student_grades[student] = 'Fail'


# print(student_grades)


# for item in student_grades.items():
#     print(item)

# print(student_grades.itemsview())

# travel_log =  [
#     {
#         'country':'France',
#      'cities_visited': ['Paris', 'Lille', 'Dijon'], 
#      'total_visits': 12
#      },
#      {
#          'country': 'France',
#          'cities_visited': ['Berlin', 'Hamburg', 'Stuttgart'],
#          'total_visits': 5
#      }
# ]

# country = input('Enter country visited: \n' )
# places_visited = input('Enter the cities you visited separated by commas: \n').split()
# num_of_visits = input('How many visits did you make in total? \n')


# def add_new_country(country, num_visits, places_visited):
#     country = country
#     num_visits = num_visits
#     places_visited = places_visited

#     travel_dict = {}
#     travel_dict['country'] = country
#     travel_dict['cities_visited'] = places_visited
#     travel_dict['total_visits'] = num_visits
#     travel_log.append(travel_dict)

#     print(travel_log)

# add_new_country(country=country, num_visits=num_of_visits, places_visited=places_visited)