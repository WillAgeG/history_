import streamlit as st
import pandas as pd
import plotly.express as px
import pydeck as pdk

def main():
    # Заголовок приложения
    st.title('Интерактивная история Второй мировой войны')

    # Загрузка данных
    data = load_data()

    # Боковая панель фильтров
    filtered_data = sidebar_filters(data)

    # Вкладки для навигации
    tabs(filtered_data)

def load_data():
    # Встроенные данные о событиях
    data = pd.DataFrame([
        {'Дата': '1939-09-01', 'Событие': 'Начало Второй мировой войны', 'Страна': 'Польша', 'Тип события': 'Военные действия', 'Описание': 'Вторжение Германии в Польшу', 'Широта': 52.2297, 'Долгота': 21.0122},
        {'Дата': '1939-09-17', 'Событие': 'Вторжение СССР в Восточную Польшу', 'Страна': 'Польша', 'Тип события': 'Военные действия', 'Описание': 'Советские войска входят в восточные регионы Польши', 'Широта': 52.2297, 'Долгота': 21.0122},
        {'Дата': '1940-05-10', 'Событие': 'Вторжение в Бельгию', 'Страна': 'Бельгия', 'Тип события': 'Военные действия', 'Описание': 'Германия вторгается в Бельгию и Нидерланды', 'Широта': 50.8503, 'Долгота': 4.3517},
        {'Дата': '1941-06-22', 'Событие': 'Операция "Барбаросса"', 'Страна': 'СССР', 'Тип события': 'Военные действия', 'Описание': 'Начало немецкого вторжения в Советский Союз', 'Широта': 55.7558, 'Долгота': 37.6173},
        {'Дата': '1941-08-14', 'Событие': 'Подписание Атлантической хартии', 'Страна': 'СССР', 'Тип события': 'Политические события', 'Описание': 'Согласование целей войны между США и Великобританией, присоединение СССР', 'Широта': 55.7558, 'Долгота': 37.6173},
        {'Дата': '1943-02-02', 'Событие': 'Капитуляция немецких войск в Сталинграде', 'Страна': 'СССР', 'Тип события': 'Политические события', 'Описание': 'Окончание Сталинградской битвы, поворотный момент войны', 'Широта': 48.7080, 'Долгота': 44.5133},
        {'Дата': '1944-06-06', 'Событие': 'Высадка в Нормандии', 'Страна': 'Франция', 'Тип события': 'Военные действия', 'Описание': 'Открытие Второго фронта в Европе', 'Широта': 49.4431, 'Долгота': -1.2290},
        {'Дата': '1945-05-08', 'Событие': 'День Победы в Европе', 'Страна': 'Германия', 'Тип события': 'Конец войны', 'Описание': 'Официальная капитуляция Германии', 'Широта': 52.5200, 'Долгота': 13.4050},
        {'Дата': '1945-09-02', 'Событие': 'Официальная капитуляция Японии', 'Страна': 'Япония', 'Тип события': 'Конец войны', 'Описание': 'Подписание акта о капитуляции на борту "Миссури"', 'Широта': 35.6895, 'Долгота': 139.6917},
        {'Дата': '1942-08-23', 'Событие': 'Начало Сталинградской битвы', 'Страна': 'СССР', 'Тип события': 'Военные действия', 'Описание': 'Одно из самых крупных сражений Второй мировой войны', 'Широта': 48.7080, 'Долгота': 44.5133},
        {'Дата': '1943-07-05', 'Событие': 'Битва на Курской дуге', 'Страна': 'СССР', 'Тип события': 'Военные действия', 'Описание': 'Крупнейшее танковое сражение в истории', 'Широта': 51.7191, 'Долгота': 36.1914},
        {'Дата': '1945-04-30', 'Событие': 'Смерть Гитлера', 'Страна': 'Германия', 'Тип события': 'Политические события', 'Описание': 'Гитлер совершает самоубийство в бункере', 'Широта': 52.5200, 'Долгота': 13.4050},
        {'Дата': '1945-08-06', 'Событие': 'Бомбардировка Хиросимы', 'Страна': 'Япония', 'Тип события': 'Военные действия', 'Описание': 'Сброс первой атомной бомбы на Хиросиму', 'Широта': 34.3853, 'Долгота': 132.4553},
        {'Дата': '1945-08-09', 'Событие': 'Бомбардировка Нагасаки', 'Страна': 'Япония', 'Тип события': 'Военные действия', 'Описание': 'Сброс второй атомной бомбы на Нагасаки', 'Широта': 32.7503, 'Долгота': 129.8777},
        {'Дата': '1941-12-07', 'Событие': 'Нападение на Перл-Харбор', 'Страна': 'США', 'Тип события': 'Военные действия', 'Описание': 'Япония атакует военно-морскую базу Перл-Харбор', 'Широта': 21.3069, 'Долгота': -157.8583},
        # Добавьте дополнительные события для расширения функционала
        {'Дата': '1942-01-01', 'Событие': 'Подписание Декларации Объединенных Наций', 'Страна': 'СССР', 'Тип события': 'Политические события', 'Описание': '26 стран подписывают соглашение о совместной борьбе против стран Оси', 'Широта': 55.7558, 'Долгота': 37.6173},
        {'Дата': '1945-02-04', 'Событие': 'Ялтинская конференция', 'Страна': 'СССР', 'Тип события': 'Политические события', 'Описание': 'Встреча "большой тройки" для обсуждения послевоенного устройства мира', 'Широта': 44.4970, 'Долгота': 34.1580},
    ])
    data['Дата'] = pd.to_datetime(data['Дата'])
    return data

def sidebar_filters(data):
    # Боковая панель фильтров
    st.sidebar.header('Фильтры')

    # Фильтр по дате
    start_date = st.sidebar.date_input('Начальная дата', data['Дата'].min())
    end_date = st.sidebar.date_input('Конечная дата', data['Дата'].max())

    # Фильтр по странам
    countries = st.sidebar.multiselect('Страны', sorted(data['Страна'].unique()), sorted(data['Страна'].unique()))

    # Фильтр по типу события
    event_types = st.sidebar.multiselect('Типы событий', sorted(data['Тип события'].unique()), sorted(data['Тип события'].unique()))

    # Поиск по ключевым словам
    keyword = st.sidebar.text_input('Поиск по описанию событий')

    # Применение фильтров
    filtered_data = data[
        (data['Дата'] >= pd.to_datetime(start_date)) &
        (data['Дата'] <= pd.to_datetime(end_date)) &
        (data['Страна'].isin(countries)) &
        (data['Тип события'].isin(event_types))
    ]

    if keyword:
        filtered_data = filtered_data[filtered_data['Описание'].str.contains(keyword, case=False)]

    # Кнопка сброса фильтров
    if st.sidebar.button('Сбросить фильтры'):
        st.experimental_rerun()

    return filtered_data

def tabs(filtered_data):
    # Вкладки для навигации
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["События", "Статистика", "Карта", "Таймлайн", "Аналитика"])

    # Вкладка "События"
    with tab1:
        show_events(filtered_data)

    # Вкладка "Статистика"
    with tab2:
        show_statistics(filtered_data)

    # Вкладка "Карта"
    with tab3:
        show_map(filtered_data)

    # Вкладка "Таймлайн"
    with tab4:
        show_timeline(filtered_data)

    # Вкладка "Аналитика"
    with tab5:
        show_analysis(filtered_data)

def show_events(filtered_data):
    st.header('События')
    st.write(f"Найдено событий: {filtered_data.shape[0]}")

    if filtered_data.empty:
        st.warning('По заданным фильтрам событий не найдено.')
        return

    # Кнопка для отображения данных в таблице
    if st.checkbox('Показать данные в виде таблицы'):
        st.dataframe(filtered_data)

    # Экспорт данных
    if st.button('Экспортировать данные в CSV'):
        csv = filtered_data.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Скачать CSV",
            data=csv,
            file_name='filtered_events.csv',
            mime='text/csv',
        )

    # Вывод деталей каждого события
    for index, row in filtered_data.iterrows():
        st.subheader(row['Событие'])
        st.write(f"**Дата:** {row['Дата'].strftime('%Y-%m-%d')}")
        st.write(f"**Страна:** {row['Страна']}")
        st.write(f"**Тип события:** {row['Тип события']}")
        st.write(row['Описание'])
        st.markdown('---')

def show_statistics(filtered_data):
    st.header('Статистика')

    if filtered_data.empty:
        st.warning('По заданным фильтрам данных для статистики нет.')
        return

    # График распределения событий по странам
    country_counts = filtered_data['Страна'].value_counts()
    if not country_counts.empty:
        fig_country = px.bar(
            x=country_counts.index,
            y=country_counts.values,
            labels={'x': 'Страна', 'y': 'Количество событий'},
            title='Распределение событий по странам'
        )
        st.plotly_chart(fig_country)
    else:
        st.info('Нет данных для отображения графика по странам.')

    # График распределения событий по типам
    type_counts = filtered_data['Тип события'].value_counts()
    if not type_counts.empty:
        fig_type = px.pie(
            names=type_counts.index,
            values=type_counts.values,
            title='Распределение событий по типам'
        )
        st.plotly_chart(fig_type)
    else:
        st.info('Нет данных для отображения графика по типам событий.')

def show_map(filtered_data):
    st.header('Карта событий')

    if filtered_data.empty:
        st.warning('По заданным фильтрам событий для отображения на карте нет.')
        return

    # Проверка наличия координат
    if 'Широта' in filtered_data.columns and 'Долгота' in filtered_data.columns:
        # Переименовываем столбцы для st.map()
        map_data = filtered_data.rename(columns={'Широта': 'latitude', 'Долгота': 'longitude'})
        st.map(map_data[['latitude', 'longitude']])

        # Альтернативный вариант с использованием pydeck
        layer = pdk.Layer(
            'ScatterplotLayer',
            data=map_data,
            get_position='[longitude, latitude]',
            get_radius=50000,
            get_color=[255, 0, 0],
            pickable=True
        )

        view_state = pdk.ViewState(
            latitude=map_data['latitude'].mean(),
            longitude=map_data['longitude'].mean(),
            zoom=2
        )

        r = pdk.Deck(layers=[layer], initial_view_state=view_state, tooltip={"text": "{Событие}\n{Дата}"})
        st.pydeck_chart(r)
    else:
        st.warning('Координаты событий недоступны.')

def show_timeline(filtered_data):
    st.header('Таймлайн событий')

    if filtered_data.empty:
        st.warning('По заданным фильтрам событий для таймлайна нет.')
        return

    # Группировка событий по годам
    timeline_data = filtered_data.copy()
    timeline_data['Год'] = timeline_data['Дата'].dt.year
    events_by_year = timeline_data.groupby('Год')['Событие'].count().reset_index()

    if not events_by_year.empty:
        fig_timeline = px.line(events_by_year, x='Год', y='Событие', labels={'Событие': 'Количество событий'}, title='Количество событий по годам')
        st.plotly_chart(fig_timeline)
    else:
        st.info('Нет данных для отображения таймлайна.')

    # Отображение событий в хронологическом порядке
    sorted_data = filtered_data.sort_values('Дата')
    for index, row in sorted_data.iterrows():
        st.write(f"**{row['Дата'].strftime('%Y-%m-%d')}:** {row['Событие']}")

def show_analysis(filtered_data):
    st.header('Аналитика')

    if filtered_data.empty:
        st.warning('По заданным фильтрам данных для аналитики нет.')
        return

    # Пример дополнительного анализа: среднее количество событий по годам
    timeline_data = filtered_data.copy()
    timeline_data['Год'] = timeline_data['Дата'].dt.year
    events_by_year = timeline_data.groupby('Год')['Событие'].count().reset_index()
    avg_events = events_by_year['Событие'].mean()
    st.write(f"**Среднее количество событий в год:** {avg_events:.2f}")

    # Топ-5 стран по количеству событий
    country_counts = filtered_data['Страна'].value_counts().head(5)
    if not country_counts.empty:
        st.subheader('Топ-5 стран по количеству событий')
        st.bar_chart(country_counts)
    else:
        st.info('Нет данных для отображения топ-5 стран.')

    # Распределение событий по месяцам
    filtered_data['Месяц'] = filtered_data['Дата'].dt.month
    events_by_month = filtered_data['Месяц'].value_counts().sort_index()
    if not events_by_month.empty:
        fig_month = px.bar(
            x=events_by_month.index,
            y=events_by_month.values,
            labels={'x': 'Месяц', 'y': 'Количество событий'},
            title='Распределение событий по месяцам'
        )
        st.plotly_chart(fig_month)
    else:
        st.info('Нет данных для отображения распределения по месяцам.')

if __name__ == "__main__":
    main()
