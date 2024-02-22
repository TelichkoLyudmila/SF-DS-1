# 8. Дипломный проект. Бриф «Лаборатории исследований гражданского общества». Определение уязвимых групп населения

## Оглавление  
1. Описание проекта
2. Какой кейс решаем?
3. Краткая информация о данных
4. Этапы работы над проектом
5. Результат
6. Выводы

### Описание проекта    
  
До 2021 года «черта бедности» (жизнь на сумму ниже прожиточного минимума) в России определялась стоимостью минимальной продуктовой корзины. В том же году правительство «отвязало» уровень бедности от цен на базовые продукты: с 2021 года прожиточный минимум рассчитывается как 44.2 % от медианного дохода граждан РФ за прошлый год.

В связи с этим необходимо с помощью кластеризации выделить, какие регионы попадают в наиболее уязвимые группы населения

### Какой кейс решаем?    

С помощью методов машинного обучения выделить регионы наиболее остро нуждающиеся в социальной поддержке на основании общедоступных данных государственной статистики

**Условия соревнования:**  
Необходимо:
- кластеризовать регионы России и определить, какие из них наиболее
остро нуждаются в помощи малообеспеченным/неблагополучным
слоям населения;
- описать группы населения, сталкивающиеся с бедностью;
- определить:
    - влияет ли число детей, пенсионеров и других социально уязвимых
групп на уровень бедности в регионе;
    - связаны ли уровень бедности/социального неблагополучия с
производством и потреблением в регионе;
    - какие ещё зависимости можно наблюдать относительно
социально незащищённых слоёв населения.

**Метрика качества**     
Коэффициент силуэта и возможность использовать кластеризацию для целей проекта

**Что практикуем**     
Feature engineering, стандартизация, кластеризация, визуализация (в т.ч. по геометкам)

### Краткая информация о данных
Данные собраны из официальной статистики за 2017-2022 гг. В некоторых показателях на момент 31.01.2024 еще не было данных за 2022 г.

- child_mortality_rural - Число умерших на первом году жизни детей за год (человек) в сельской местности
- child_mortality_urban - Число умерших на первом году жизни детей за год (человек) в городской местности
- nominal_income - Среднедушевые денежные доходы (в месяц), руб.
- real_income_to_previos_year - Реальные денежные доходы, в процентах к предыдущему году		
- avg_population - Численность постоянного населения в среднем за год		
- disability - Общая численность инвалидов	
- disease - Заболеваемость на 1000 человек	- рассчитывается как отношение числа первичных обращений к средней численности населения, умноженное на 1000
- gross_regional_product - Валовой региональный продукт на душу населения до 2021	
- housing_on_one_person - Общая площадь жилых помещений, приходящаяся в среднем на одного жителя (кв.м.)
- natural_population_groth - Естественный прирост за год	
- people_lower_poverty_line - Численность населения с доходами ниже линии бедности
- disabled_population - Доля нетрудоспособного населения в регионах
	- poverty_socdem_2017 - 2021 - Распределение малоимущего населения по социально-демографическим группам(процент, значение показателя за год)
- retail_turnover_per_capita - Оборот розничной торговли на душу населения (рубль, значение показателя за год)
- unemployed - Численность безработных граждан, зарегистрированных в государственных учреждениях службы занятости населения и получающих социальные выплаты (человек)
- workers - Отношение числа занятых в экономике региона к численности населения региона в трудоспособном возрасте (процент)
- welfare_expense_share - Удельный вес расходов на социальную политику в общем объеме расходов консолидированных бюджетов субъектов РФ (в %)
- crime_total - Всего зарегистрировано преступлений	
- crime_economical - Выявлено лиц, совершивших преступления экономической направленности	
- crime_without_income  - Выявлено лиц, совершивших преступления, не имеющих постоянного источника дохода


### Этапы работы над проектом  
1. Сбор и обработка данных. \
1.1. Импорт и приведение к единому виду столбцов\
1.2. Выбор необходимых регионов, приведение к единому виду названий\
1.3. Сведение в единый датасет\
1.4. Очистка от пропусков\
1.5. Датасет с относительными величинами\
1.6. Приведение всех признаков к формату "чем больше, тем лучше"\
1.7. Формирование датасетов по годам
2. Разведывательный анализ данных\
2.1. Ключевые описательные статистики\
2.2. Визуализация относительных признаков\
2.3. Визуализация абсолютных признаков\
2.4. Регионы, имеющие проблемы в большинстве признаков
3. Анализ взаимозависимости признаков\
3.1. Корреляционная матрица для датасета с относительными признаками\
3.2. Корреляционная матрица для датасета с абсолютными признаками\
3.3. Подготовка к кластеризации - стандартизация
4. Кластеризация\
4.1. K-means\
4.2. Иерархическая кластеризация\
4.3. DBSCAN\
4.4. Понижение размерности - PCA\
4.4.1 PCA - K-means\
4.4.2 PCA - Иерархическая кластеризация\
4.5 Понижение размерности t-SNE\
4.5.1 t-SNE - K-means\
4.5.2 t-SNE - Иерархическая кластеризация\
4.6. Свод по результатам кластеризации
5. Кластеризация за все годы наблюдений\
5.1. Кластеризация за 2017-2022 гг.\
5.2. График с кластеризацией регионов на карте РФ
6. Выводы

### Результаты:  

В ходе работы была выгружена свежая социальная статистика с сайтов Росстата и fedstat. После очистки и выгрузки данных, было получено 19 датасетов с регионами за период 2017-2022 г. Тут мы столкнулись с проблемой, что по сути имеем дело с признаками для кластеризации регионов и временными рядами одновременно. Можно было бы делать time series clusterisation по каждому признаку, тогда можно было бы отследить некоторые закономерности: достигаются ли одинаковые значения во времени, есть ли схожие тенденции к одновременному увеличению и уменьшению или схожие повторяющиеся закономерности в разные годы. Однако т.к. у нас статистика погодовая, и временной ряд взят не очень длинный (с 2017 года - года смены методологии рассчета Росстата), то кластеризация временных была бы не очень продуктивна. Поэтому рассматривали кластеризацию регионов по признакам.

Для итоговой кластеризации были получены отдельные датасеты за 2017-2022 г, внутри каждого были таблицы Регионы\признаки. Также для основного анализирующего датасета (на котором проверялись методы кластеризации) был взят датасет на основе среднего признака за последние 3 года (2020-2022) эти годы охватывали пандемию и начало СВО, следовательно должны довольно явно выявить нуждающиеся регионы. Также учитывая, что некоторые признаки были в натуральном(абсолютном выражении) т.е. в людях, было очевидно, что будут сильно коррелировать признаки, завязанные на численность населения. Поэтому были отдельно созданы датасеты по каждому году с относительными признаками (т.е. деленые на численность населения).

### Выводы:  
Были выявлены следующие взаимозависимости между данными:
- между признаками "Доля нетрудоспособного населения" и "доля населения с доходами ниже линии бедности" кросс-корреляция выше 90%. Это говорит о том, что с большой вероятностью эти 2 признака связаны, ведь распределение регионов по ним практически идентично. Следовательно можно сделать вывод, что если в регионе большая доля стариков и детей это приводит к серьезной нагрузке для семей, что они оказываются за линией бедности в пересчете на человека. Безусловно такие регионы очень нуждаются в мерах социальной поддержки
- корреляцию 80% имеют признаки "отношение числа занятых в экономике региона к численности населения региона в трудоспособном возрасте" и "среднедушевые денежные доходы" - тоже выглядит логично т.к. чем больше людей имеющих возможность работать, работают, тем выше среднедушевой доход (поскольку в расчете этого показателя идет полная численность населения, а не численность работющего населения). Аналогичная высокая корреляция между рабочими и ВРП - принцип объяснения такой же (чем больше рабочих, тем выше ВРП на душу населения). Возможно, некоторые из этих признаков будут в дальнейшем исключены, т.к. они в целом объясняют регионы в схожем ключе
- менее 90%, но также высокая обратная корреляция между признаками "общая площадь жилых помещений, приходящаяся в среднем на одного жителя" и "коэффициент естественного прироста". Т.е. чем больше убыль населения, тем больше кв.м. приходится на 1 человека - выглядит закономерно. 
- интересная взаимосвязь с признаком welfare_expense_share (Удельный вес расходов на социальную политику в общем объеме расходов консолидированных бюджетов субъектов РФ): средне-высокая обратная корреляция с признаками среднедушевого денежного дохода, ВРП и доли работающего населения из трудоспособного (эти же показатели между собой тоже сильно скоррелированы). Можно предположить, что во многом социальная поддержка распределяется во многом основываясь на этой официальной статистике.
- Численность населения с доходами ниже линии бедности имеют достаточно высокую обратную корреляцию с оборотом розничной торговли на душу населения. Что в целом логично: чем меньше уровень заработка населения в регионе, тем меньший вклад в развитие региона (в частности торговлю) население вносит.
- Чем больше население, тем больше преступлений в натуральном выражении. Заметим, что средняя обратная корреляция наблюдается между этим признаком и всеми 3-мя видами престплений, что в целом тоже объяснимо учитывая минусовой естественный прирост.


До начала кластеризации были выделены регионы, которые попадали в нижние 10% каждого признака, (т.е. регионы с самой плачевной ситуацией по каждому признаку) и на этом этапе мы заметили, что помимо дотационных регионов в список попал Ненецкий округ. После проведения кластеризации мы получили очень схожие результаты: в 2 наименьших класса попали те же дотационные регионы, Ненецкий и Ямало-Ненецкий ао. Многие из них лидируют в таких показателях как минимальные доход на душу населения, минимальная площадь на человека, максимумы по детской смертности, болезням и многим другим показателям.

Что касается Ненецкого и Ямало-Ненецкого округов - несмотря на то, что это ресурсные регионы, в которых большие доходы населения связаны с добываемыми полезными ископаемыми (они попадают в топ с самый высокий ВРП на душу населения). Это также регионы с очень дорогой себестоимостью жизни и высокими показателями социальных проблем в пересчете на небольшое население региона. Неожиданно эти же регионы лидируют по доли инвалидов на население региона. Так Ненецкий регион входит в 10% наихудших по показателям pаболеваемости на 1000 человек, общей численности инвалидов, доли людей за гранью бедности и экономических преступлений. А Ямало-Ненецкий в том же топе по болезням и минимальной доступности жилья. И также оба эти региона входят в 10% минимальных процентов по соцподдержке, выделяемых из средств региона. По сути довольно неожиданным выводом является то, что регион может иметь высокие ВРП и доход на душу населения, но из-за других факторов (не учтенных в соц.выплатах) нуждаться в доп. поддержке населения. **В итоге выделены регионы, которые по итогам исследований, нуждаются в поддержке населения больше других: Камчатский край, Магаданская область, Ненецкий автономный округ, Республика Алтай, Республика Ингушетия, Республика Тыва, Чеченская Республика, Чукотский автономный округ, Ямало-Ненецкий автономный округ.**