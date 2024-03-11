# 9. Оптимальная стратегия подъема статуса с общего пользователя до 9 VIP-статуса на Binance для компании алгоритмического трейдинга

## Оглавление  
1. Описание проекта
2. Какой кейс решаем? 
3. Краткая информация о данных
4. Этапы работы над проектом
5. Результат  
6. Выводы

### Описание проекта    
  
Суть кейса в выведении оптимальной стратегии подъема статуса с общего пользователя до 9 VIP-статуса на Binance для компании алгоритмического трейдинга на примере Spot-торговли

### Какой кейс решаем?    
Изначально попробуем выгрузить информацию с сайта Binance о VIP-статусах, рассчитать оптимальный путь роста с учетом комиссий при прочих равных

### Краткая информация о данных
Данные о VIP-статусах берем с официального сайта Binance: https://www.binance.com/en/fee/trading

### Этапы работы над проектом  

1. Выгрузка данных по url
2. Преобразования данных
3. Поиск оптимальной комбинации повышения статусов для Maker\
    3.1. Пул комбинаций статусов\
    3.2. Максимальный объем\
    3.3. Механика расчета
4. Расчет оптимальной стратегии подъема статуса для Taker

### Результаты:  

Мы выяснили, что если используем только стратегию Maker, то оптимальным темпом поднятия статуса будет: 0, 1, 3, 5, 7, 9. И минимальный fee, уплаченный бирже будет 163060000$, что составляет 2.18% от общей вложенной суммы. После достижения 9 статуса, fee уже будет минимальным и средняя ставка будет снижаться. Безусловно, расчет комиссий упрощен и не учитывает другие факторы, такие как объем торговли, частота сделок и динамика рынка. Также мы не закладываем сюда ожидаемую доходность от актива, и тот факт, что чем дольше мы будем идти к 9 статусу, тем больше альтернативных вложений потеряем. Однако подобный подход позволил математически расчитать самый выгодный способ повышения уровня для Maker стратегии.

Для Taker оптимальной стратегией будет перескочить 1 уровень, т.е. 0, 3, 5, 7, 9 (вероятно из-за того, что для Taker VIP-0 и VIP-1 имеют одинаковую ставку комиссии) и суммарная комиссия, уплаченная бирже составит 3,39%, что в целом ожидаемо выше, чем у Maker потому что Taker-операции снижают ликвидность. Аналогично можно использовать эту функцию для USD или фьючерсов.

### Выводы:  
Мы вывели универсальный алгоритм для подъема VIP-статуса с общего пользователя до 9-VIP-статуса с минимальными потерями в комисии. Также убедились, что для разных стратегий и комиссий эта схема будет отличаться. В дальнейшем используя эту же функцию можно просчитать и более сложные стратегии, например различные комбинации Maker-Taker, или использовать комиссии для других рынков. Задача будет только в том, чтобы правильно расчитать ожидаемую доходность и скорректировать столбец rates для расчетов.

