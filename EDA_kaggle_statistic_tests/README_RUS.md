# Статистические тесты в контексте EDA по з/п в Data Science

## Оглавление  
1. Описание проекта
2. Какой кейс решаем? 
3. Краткая информация о данных
4. Этапы работы над проектом
5. Результат  
6. Выводы

### Описание проекта    
HR-агентство изучает тренды на рынке труда в IT. Компания хочет провести исследование на основе данных о зарплатах в сфере Data Science за 2020–2022 годы и получить некоторые выводы.

Суть кейса в ответе на вопросы касательно вакансий в Data Sciense и определении, значимы ли статистически полученные ответы

### Какой кейс решаем?    
- Наблюдается ли ежегодный рост зарплат у специалистов Data Scientist?
- Влияет ли опыт работы ('experience_level') на зарплату у специалистов Data Scientist?
- Влияет ли тип занятости ('employment_type') на зарплату у специалистов Data Scientist?
- Влияет ли доля удаленной работы ('remote_ratio') на зарплату у специалистов Data Scientist?
- Влияет ли размер компании ('company_size') на зарплату у специалистов Data Scientist?
- Влияет ли локация сотрудника (расположен он в одном и том же регионе, что и работодатель или нет) на его заработную плату?
- Влияет ли локация сотрудника (расположен он в одном и том же регионе, что и работодатель или нет) на его объем удаленной работы?
- Как соотносятся зарплаты Data Scientist и Data Engineer в различных компаниях?
- Есть ли связь между наличием должностей Data Scientist и Data Engineer и размером компании?

**Что практикуем**     
статистический анализ данных, построение гипотез, тесты на нормальность

### Краткая информация о данных
Оригинальный датасет: “Data Science Job Salaries” (kaggle.com)

Таблица:
- work_year	Год, в котором была выплачена зарплата.

- experience_level	Опыт работы на этой должности в течение года со следующими возможными значениями:\
EN — Entry-level/Junior;\
MI — Mid-level/Intermediate;\
SE — Senior-level/Expert;\
EX — Executive-level/Director.

- employment_type	Тип трудоустройства для этой роли:\
PT — неполный рабочий день;\
FT — полный рабочий день;\
CT — контракт;\
FL — фриланс.

- job_title	Роль, в которой соискатель работал в течение года.

- salary	Общая выплаченная валовая сумма заработной платы.

- salary_currency	Валюта выплачиваемой заработной платы в виде кода валюты ISO 4217.

- salary_in_usd	Зарплата в долларах США (валютный курс, делённый на среднее значение курса доллара США за соответствующий год через fxdata.foorilla.com).

- employee_residence	Основная страна проживания сотрудника в течение рабочего года в виде кода страны ISO 3166.

- remote_ratio	Общий объём работы, выполняемой удалённо. Возможные значения:\
0 — удалённой работы нет (менее 20 %);\
50 — частично удалённая работа;\
100 — полностью удалённая работа (более 80 %).

- company_location	Страна главного офиса работодателя или филиала по контракту в виде кода страны ISO 3166.

- company_size	Среднее количество людей, работавших в компании в течение года:\
S — менее 50 сотрудников (небольшая компания);\
M — от 50 до 250 сотрудников (средняя компания);\
L — более 250 сотрудников (крупная компания).

### Этапы работы над проектом  
1. Разведывательный анализ данных
2. Статистический анализ данных

### Результаты:  

*   Наблюдается ли ежегодный рост зарплат у специалистов Data Scientist?\
ЗП отличается год к году, однако рост с 2020 на 2021 г. не очевиден, а вот рост ЗП в сфере Data Science с 2021 на 2022 г. явно был

*   Влияет ли опыт работы ('experience_level') на зарплату у специалистов Data Scientist?\
По мере роста экспертности в сфере Data Science ЗП специалистов действительно растет

*   Влияет ли тип занятости ('employment_type') на зарплату у специалистов Data Scientist?\
Мы можем наверняка говорить только про полную и неполную занятость - ЗП при неполной занятости ниже. Про связь остальных типов занятости ничего точно сказать нельзя

*   Влияет ли доля удаленной работы ('remote_ratio') на зарплату у специалистов Data Scientist?\
Можно сделать вывод, что объем удаленной работы действительно связан с объемом ЗП, но логика нелинейная: больше всего ЗП у тех, кто работает 100% на удаленке, потом идут те, кто практически не имеет удаленной работы, а вот заработок тех, у кого в удаленном формате половина работы - самый низкий

*   Влияет ли размер компании ('company_size') на зарплату у специалистов Data Scientist?\
Можно заключить, что размер компании действительно влияет на ЗП сотрудников: малые компании платят меньше, чем средние и крупные. Однако, кто между M и L лидирует наверняка сказать нельзя

*   Влияет ли локация сотрудника (расположен он в одном и том же регионе, что и работодатель или нет) на его заработную плату?\
Действительно, если компания и сотрудник находятся в одном регионе, сотрудник может получать больше, чем когда они находятся в разных

*   Влияет ли локация сотрудника (расположен он в одном и том же регионе, что и работодатель или нет) на его объем удаленной работы?\
Не существует статистически значимой взаимосвязи между расположением сотрудника относительно работодателя и его объемом удаленной работы

*   Как соотносятся зарплаты Data Scientist и Data Engineer в различных компаниях?\
ЗП в сферах Data Scientist и Data Engineer не имеют статистически значимой разницы

*   Есть ли связь между наличием должностей Data Scientist и Data Engineer и размером компании?\
Нет статистически значимой связи между наличием должностей Data Scientist и Data Engineer и размером компании

### Выводы:  
Удалось ответить на каждый вопрос и понять, значим ли первичный ответ статистически

