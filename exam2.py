#   Функция будет использовать метод _count_salary_ для каждого объекта

def count_all_salaries(workers_dict):
  total_spendnings=0
  for worker in workers_dict:      # (Только у продавца есть отдельный метод)
    our_dict=workers_dict[worker]
    class1=eval(our_dict['sample'])        # Превращаем строку в класс
    if class1.type_of_salary=='salary&comissions':
      class1._count_salary_(class1.type_of_salary,our_dict['salary'],our_dict['working hours'],our_dict['number of total sales'])

    else:
      class1._count_salary_(class1.type_of_salary,our_dict['salary'],our_dict['working hours'])
    total_spendnings+=class1.salary
    print(f'{worker}\' salary  -  {class1.salary}')
  return (f'\nThe sum of all the salaries : {total_spendnings}')

#   Функция будет использовать метод productivity для каждого объекта

def productiveness_program(workers_dict):
  productive_dict={}
  for person in workers_dict:
    class1=eval(workers_dict[person]['sample'])
    class1.productivity(workers_dict[person]['working hours'])
    productive_dict[class1.last_name]=class1.productiveness
    
  productive_dict=sorted(productive_dict.items(), key=lambda item: item[1],reverse=True)    # Сортируем словарь , чтобы получить рейтинг продуктивности
  productive_list=[i for i in productive_dict]
  print(f'The most productive worker is {productive_list[0][0]}')
  print(f'The least productive worker is {productive_list[-1][0]}\n{productive_list[-1][0]} , you need to work more !')



class Worker:
  def __init__(self,last_name,id):
    self.last_name=last_name
    self.id=id
  def _count_salary_(self,type_of_salary,salary,working_hours):    
    if self.type_of_salary=='fixed':
      self.salary=salary

    elif self.type_of_salary=='per hour':
      self.salary=salary*working_hours
      #Зарплату продавца нужно считать в классе самого продавца,иначе нельзя передать аргумент с количством проданных товаров
  def productivity(self,working_hours):
    self.productiveness=working_hours/40


class Manager(Worker):  
  def __init__(self,last_name,id):
    super().__init__(last_name,id)  #Указываем , какой вид оплаты у каждой профессии
    self.type_of_salary='fixed'

class Secretary(Worker):
  def __init__(self,last_name,id):
    super().__init__(last_name,id)
    self.type_of_salary='fixed'

class Saler(Worker):        #У продавца меняем метод , т.к у него есть добавочный аргумент - аргумент проданных товаров
  def __init__(self,last_name,id):
      super().__init__(last_name,id)
      self.type_of_salary='salary&comissions'

  def _count_salary_(self,type_of_salary,salary,working_hours,num_of_sales):
    super()._count_salary_(type_of_salary,salary,working_hours)
    self.salary=salary+50*num_of_sales
    return self.salary

class ShopWorker(Worker):
  def __init__(self,last_name,id):
      super().__init__(last_name,id)
      self.type_of_salary='per hour'

class TemporarySecretary(Secretary): # Наследственный класс от класса секретаря(меняем вид оплаты)
  def __init__(self,last_name,id):
      super().__init__(last_name,id)
      self.type_of_salary='per hour'


manager1=Manager('Канаткулов',1)

secretary1=Secretary('Тилекбаев',2)

saler1=Saler('Шалымбекова',3)

shop_worker1=ShopWorker('Бакыт Рустамов',4)

shop_worker2=ShopWorker('Алтынай Ширинбаева',5)

temp_secretary1=TemporarySecretary('Рыскулов',6)
  
  #   Создаем словарь из всех сотрудников , т.к в функциях count_all_salaries иproductiveness_program нужны добавочные аргументы для некоторых работников , и мы исользуем другие методы их классов ,которые требуют других аргументов(working hours etc.)
workers_dict={
  'Барсбек Канаткулов':{'sample':'manager1','salary':45000,'working hours':18},
  'Алымкул Тилекбаев':{'sample' : 'secretary1','salary':20000,'working hours':38},
  'Айпери Шалымбекова':{'sample' : 'saler1','salary':20000,'working hours':38,'number of total sales':20},
  'Бакыт Рустамов':{'sample' : 'shop_worker1','salary':100,'working hours':25},    
  'Алтынай Ширинбаева':{'sample' : 'shop_worker2','salary':100,'working hours':40},
  'Жанар Рыскулов':{'sample' : 'temp_secretary1','salary':100,'working hours':33},
}
print(count_all_salaries(workers_dict))
print()
productiveness_program(workers_dict)



