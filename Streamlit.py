import altair as alt
import pandas as pd
import streamlit as st
import numpy as np
import requests # library to handle requests
import folium # map rendering library
from streamlit_folium import folium_static 
import json



PAGES = ['Sin MFC: Costo Mayo',
    'MFC 100% : 650 Pedidos Diarios',
    'MFC 1000 Pedidos: Ruta Mirador',
    'MFC 1000 Pedidos: Hub & Spoke',
    'MFC 2000 Pedidos'
]

def run_UI():
    st.set_page_config(
        page_title="Estudio de MFC",
        page_icon="🏠",
        initial_sidebar_state="expanded",
        menu_items={
            'Report a bug': "https://github.com/arup-group/social-data/issues/new/choose",
            'About': """            
         If you're seeing this, we would love your contribution! If you find bugs, please reach out or create an issue on our 
         [GitHub](https://github.com/arup-group/social-data) repository. If you find that this interface doesn't do what you need it to, you can create an feature request 
         at our repository or better yet, contribute a pull request of your own. You can reach out to the team on LinkedIn or 
         Twitter if you have questions or feedback.
    
        More documentation and contribution details are at our [GitHub Repository](https://github.com/arup-group/social-data).
        
         This app is the result of hard work by our team:
        - [Jared Stock 🐦](https://twitter.com/jaredstock) 
        - [Angela Wilson 🐦](https://twitter.com/AngelaWilson925) (alum)
        - Sam Lustado
        - Lingyi Chen
        - Kevin McGee (alum)
        - Jen Combs
        - Zoe Temco
        - Prashuk Jain (alum)
        - Sanket Shah (alum)
        Special thanks to Julieta Moradei and Kamini Ayer from New Story, Kristin Maun from the city of Tulsa, 
        Emily Walport, Irene Gleeson, and Elizabeth Joyce with Arup's Community Engagment team, and everyone else who has given feedback 
        and helped support this work. Also thanks to the team at Streamlit for their support of this work.
        The analysis and underlying data are provided as-is as an open source project under an [MIT license](https://github.com/arup-group/social-data/blob/master/LICENSE). 
        Made by [Arup](https://www.arup.com/).
        """
        }
    )
    st.sidebar.title('Estudio de MFC')
    
    page=st.sidebar.radio('Modelos Operativos', PAGES, index=1)
    
    st.experimental_set_query_params(page=page)


    if page == 'Sin MFC: Costo Mayo':
        st.sidebar.write("""
            ### Costo Mayo
            

        """)
        st.header("Costo Operacion Logistica Mayo  ", )

        
        original_title = '<p style="color:Black; font-size: 20px;">KPIs</p>'
        st.markdown(original_title, unsafe_allow_html=True)
        
        col1, col2, col3= st.columns(3)
        col1.metric("Ticket Promedio", "$45.459")
        col2.metric("% Costo de la Venta", "30%", )
        col3.metric("Ordenes", "280")



        map_sby = folium.Map(location=[-33.439445474052995, -70.65461676222148], zoom_start=10)
        data_geo = json.load(open('Unimarc.geojson'))

        original_title = '<p style="color:Black; font-size: 20px;">Mapa de Santiago</p>'
        st.markdown(original_title, unsafe_allow_html=True)

        tooltip = "MFC"
        folium.Marker([-33.35674849571172, -70.54006548079522], popup="<i>Mt. Hood Meadows</i>", tooltip=tooltip).add_to(map_sby)

        ### Anillo 1 
        data_geo = json.load(open('Unimarc.geojson'))
        features = []
        for x in data_geo['features']:
            if x['properties']['name'] in  ('Militares','Cordillera'):
                features.append(x)
    
        gson_anillo_1 = {'type':'FeatureCollection','features':features}
        maps= folium.Choropleth(geo_data = gson_anillo_1,
                           fill_color='green',
                           highlight=True,
                           reset=True).add_to(map_sby)

        ### Anillo 2
        data_geo = json.load(open('Unimarc.geojson'))
        features = []
        for x in data_geo['features']:
            if x['properties']['name'] in  ('Consistorial'):
                features.append(x)
    
        gson_anillo_2 = {'type':'FeatureCollection','features':features}
        maps= folium.Choropleth(geo_data = gson_anillo_2,
                           fill_color='blue',
                           highlight=True,
                           reset=True).add_to(map_sby)
        
        ### Anillo 2
        data_geo = json.load(open('Unimarc.geojson'))
        features = []
        for x in data_geo['features']:
            if x['properties']['name'] in  ('Huechuraba'):
                features.append(x)
    
        gson_anillo_2 = {'type':'FeatureCollection','features':features}
        maps= folium.Choropleth(geo_data = gson_anillo_2,
                           fill_color='red',
                           highlight=True,
                           reset=True).add_to(map_sby)
        
        ### Anillo 2
        data_geo = json.load(open('Unimarc.geojson'))
        features = []
        for x in data_geo['features']:
            if x['properties']['name'] in  ('Los Leones'):
                features.append(x)
    
        gson_anillo_2 = {'type':'FeatureCollection','features':features}
        maps= folium.Choropleth(geo_data = gson_anillo_2,
                           fill_color='orange',
                           highlight=True,
                           reset=True).add_to(map_sby)

        ### Anillo 3
        data_geo = json.load(open('Unimarc.geojson'))
        features = []
        for x in data_geo['features']:
            if x['properties']['name'] in  ('Mirador Externo','Mirador Centro','Mirador Norte','Mirador Sur'):
                features.append(x)
    
        gson_anillo_3 = {'type':'FeatureCollection','features':features}
        maps= folium.Choropleth(geo_data = gson_anillo_3,
                           fill_color='black',
                           highlight=True,
                           reset=True).add_to(map_sby)


        ### Anillo 4
        data_geo = json.load(open('Unimarc.geojson'))
        features = []
        for x in data_geo['features']:
            if x['properties']['name'] in  ('Camino Nos'):
                features.append(x)
    
        gson_anillo_4 = {'type':'FeatureCollection','features':features}
        maps= folium.Choropleth(geo_data = gson_anillo_4,
                           fill_color='purple',
                           highlight=True,
                           reset=True).add_to(map_sby)
        
        ### Anillo 4
        data_geo = json.load(open('Unimarc.geojson'))
        features = []
        for x in data_geo['features']:
            if x['properties']['name'] in  ('Silva Carvallo'):
                features.append(x)
    
        gson_anillo_4 = {'type':'FeatureCollection','features':features}
        maps= folium.Choropleth(geo_data = gson_anillo_4,
                           fill_color='pink',
                           highlight=True,
                           reset=True).add_to(map_sby)

        ### Anillo 4
        data_geo = json.load(open('Unimarc.geojson'))
        features = []
        for x in data_geo['features']:
            if x['properties']['name'] in  ('Mirador'):
                features.append(x)
    
        gson_anillo_4 = {'type':'FeatureCollection','features':features}
        maps= folium.Choropleth(geo_data = gson_anillo_4,
                           fill_color='yellow',
                           highlight=True,
                           reset=True).add_to(map_sby)

        folium_static(map_sby)

        col1, col2, col3, col4 = st.columns((1, 1, 1,1))
        with col1:
            original_title = '<p style="color:Green; font-weight: bold; font-size: 25px;">Militares & Cordillera </p>'
            st.markdown(original_title, unsafe_allow_html=True)
            st.write("""**Pedidos:** 51 O/D (18%)
                        **Modelo:** Shoppers""")
            st.write("""**Costo:** 15.786""")
            st.write("""**Costo x Orden:** 34%""")
            

        with col2:
            original_title = '<p style="color:Blue; font-weight: bold; font-size: 25px;">Consistorial</p>'
            st.markdown(original_title, unsafe_allow_html=True)
            st.write("""**Pedidos:** 16 O/D (6%)
                        **Modelo:** Shoppers""")
            st.write("""**Costo:** 9.782""")
            st.write("""**Costo x Orden:** 22%""")
            

        with col3:
            original_title = '<p style="color:orange; font-weight: bold; font-size: 25px;">Leones</p>'
            st.markdown(original_title, unsafe_allow_html=True)
            st.write("""**Pedidos:** 42 O/D (15%)
                        **Modelo:** Shoppers""")
            st.write("""**Costo:** 13.274""")
            st.write("""**Costo x Orden:** 29%""")
 

        with col4:
            original_title = '<p style="color:red; font-weight: bold; font-size: 25px;">Huechuraba</p>'
            st.markdown(original_title, unsafe_allow_html=True)
            st.write("""**Pedidos:** 18 O/D (6%)
                        **Modelo:** Shoppers""")
            st.write("""**Costo:** 20.961""")
            st.write("""**Costo x Orden:** 46%""")
            
        with col1:
            original_title = '<p style="color:black; font-weight: bold; font-size: 25px;">Ruta Mirador</p>'
            st.markdown(original_title, unsafe_allow_html=True)
            st.write("""**Pedidos:** 54 O/D (19%)
                        **Modelo:** Rutas """)
            st.write("""**Costo:** 16.326""")
            st.write("""**Costo x Orden:** 36%""")
        
        with col2:
            original_title = '<p style="color:yellow; font-weight: bold; font-size: 25px;">Mirador</p>'
            st.markdown(original_title, unsafe_allow_html=True)
            st.write("""**Pedidos:** 60 O/D (22%)
                        **Modelo:** Directo""")
            st.write("""**Delivery:** 8.723""")
            st.write("""**Costo x Orden:** 19%""")
     
        with col3:
            original_title = '<p style="color:pink; font-weight: bold; font-size: 25px;">Silva Carvallo</p>'
            st.markdown(original_title, unsafe_allow_html=True)
            st.write("""**Pedidos:** 31 O/D (15%)
                        **Modelo:** Directo""")
            st.write("""**Delivery:** 12.786""")
            st.write("""**Costo x Orden:** 28%""")
            
        with col4:
            original_title = '<p style="color:purple; font-weight: bold; font-size: 25px;">Camino Nos</p>'
            st.markdown(original_title, unsafe_allow_html=True)
            st.write("""**Pedidos:** 8 O/D (3%)
                        **Modelo:** Directo""")
            st.write("""**Delivery:** 18.458""")
            st.write("""**Costo x Orden:** 41%""")



    if page == 'MFC 100% : 650 Pedidos Diarios':
        st.sidebar.write("""
            ### Consideración MFC 100%
            
            **1.Transporte Ineficiente**: MFC es ineficiente en zonas lejanas por costos de transporte.

            **2.Riesgo Operacional:** Riesgo operacional bastante alto, ya que hay una alta dependencia del MFC por ser el unico punto de preparacíon de pedidos.

            **3.Mercado On-demand:** Se pierde competitividad en mercado On-demand, toda nuestra demanda seria programada.

            **4-Inflexibilidad Promocional:** Modelo no tiene holguras a periodos promocionales (high and low).   
        """)
        st.header("Demanda de 100% MFC: 650 Pedidos ", )

        
        original_title = '<p style="color:Black; font-size: 20px;">KPIs</p>'
        st.markdown(original_title, unsafe_allow_html=True)
        
        col1, col2, col3= st.columns(3)
        col1.metric("Ticket Promedio", "$45.459")
        col2.metric("% Costo de la Venta", "32%", '-30%')
        col3.metric("Ordenes", "650")



        map_sby = folium.Map(location=[-33.439445474052995, -70.65461676222148], zoom_start=10)
        data_geo = json.load(open('Unimarc.geojson'))

        original_title = '<p style="color:Black; font-size: 20px;">Mapa de Santiago</p>'
        st.markdown(original_title, unsafe_allow_html=True)

        tooltip = "MFC"
        folium.Marker([-33.35674849571172, -70.54006548079522], popup="<i>Mt. Hood Meadows</i>", tooltip=tooltip).add_to(map_sby)

        ### Anillo 1 
        data_geo = json.load(open('Unimarc.geojson'))
        features = []
        for x in data_geo['features']:
            if x['properties']['name'] in  ('Militares','Cordillera'):
                features.append(x)
    
        gson_anillo_1 = {'type':'FeatureCollection','features':features}
        maps= folium.Choropleth(geo_data = gson_anillo_1,
                           fill_color='green',
                           highlight=True,
                           reset=True).add_to(map_sby)

        ### Anillo 2
        data_geo = json.load(open('Unimarc.geojson'))
        features = []
        for x in data_geo['features']:
            if x['properties']['name'] in  ('Consistorial','Huechuraba','Los Leones'):
                features.append(x)
    
        gson_anillo_2 = {'type':'FeatureCollection','features':features}
        maps= folium.Choropleth(geo_data = gson_anillo_2,
                           fill_color='blue',
                           highlight=True,
                           reset=True).add_to(map_sby)

        ### Anillo 3
        data_geo = json.load(open('Unimarc.geojson'))
        features = []
        for x in data_geo['features']:
            if x['properties']['name'] in  ('Mirador Externo','Mirador Centro','Mirador Norte','Mirador'):
                features.append(x)
    
        gson_anillo_3 = {'type':'FeatureCollection','features':features}
        maps= folium.Choropleth(geo_data = gson_anillo_3,
                           fill_color='red',
                           highlight=True,
                           reset=True).add_to(map_sby)


        ### Anillo 4
        data_geo = json.load(open('Unimarc.geojson'))
        features = []
        for x in data_geo['features']:
            if x['properties']['name'] in  ('Silva Carvallo','Camino Nos','Mirador Sur'):
                features.append(x)
    
        gson_anillo_4 = {'type':'FeatureCollection','features':features}
        maps= folium.Choropleth(geo_data = gson_anillo_4,
                           fill_color='orange',
                           highlight=True,
                           reset=True).add_to(map_sby)

        folium_static(map_sby)

        col1, col2, col3, col4 = st.columns((1, 1, 1,1))
        with col1:
            original_title = '<p style="color:Green; font-weight: bold; font-size: 25px;">Anillo 1</p>'
            st.markdown(original_title, unsafe_allow_html=True)
            st.write("""**Pedidos:** 143 O/D (22%)
                        **Modelo:** Directo""")
            st.write("""**Delivery:** 5.750            
                        **Picking:** 3.530""")
            st.write("""**Costo x Orden:** 20%
                        **Costo Actual:** 34%""")
            

        with col2:
            original_title = '<p style="color:Blue; font-weight: bold; font-size: 25px;">Anillo 2</p>'
            st.markdown(original_title, unsafe_allow_html=True)
            st.write("""**Pedidos:** 152 O/D (23%)
                        **Modelo:** Directo""")
            st.write("""**Delivery:** 7.490            
                        **Picking:** 3.530""")
            st.write("""**Costo x Orden:** 24%
                        **Costo Actual:** 32%""")
            

        with col3:
            original_title = '<p style="color:Red; font-weight: bold; font-size: 25px;">Anillo 3</p>'
            st.markdown(original_title, unsafe_allow_html=True)
            st.write("""**Pedidos:** 222 O/D (34%)
                        **Modelo:** Directo""")
            st.write("""**Delivery:** 10.990            
                        **Picking:** 3.530""")
            st.write("""**Costo x Orden:** 32%
                        **Costo Actual:** 26%""")


        with col4:
            original_title = '<p style="color:orange; font-weight: bold; font-size: 25px;">Anillo 4</p>'
            st.markdown(original_title, unsafe_allow_html=True)
            st.write("""**Pedidos:** 133 O/D (28%)
                        **Modelo:** Directo""")
            st.write("""**Delivery:** 15.035            
                        **Picking:** 3.530""")
            st.write("""**Costo x Orden:** 41%
                        **Costo Actual:** 31%""")


    elif page == 'MFC 1000 Pedidos: Ruta Mirador':
        st.sidebar.write("""
            ### Consideración MFC 1000 Pedidos: Ruta Mirador

            **1.Zonas Cercanas:** MFC prioriza zonas cercana de influencia

            **2.On-Demand:** Tiendas del Sector oriente, destinadas exclusivamente a mercado on-demand (militares, leones, hechuraba)
            
            **3.Comunas relevantes:** Silva Carvallo, Mirador y Consistorial se abren para abastecer comunas importantes, tales como La Florida, Maipu y Peñalolen.
            
            **4.Modelo Hibrido:** Modelo Hibrido permite plan de contigencia de manera natural.
            
            **5.MultiPoligonos:** Se debe evaluar funcionalidad sistemica, para hacer competir poligonos on-demand y programados.
            
            **6.Rutas Mirador:** Puente alto, Buin, Santiago Centro, Cerro Navia son abatecidas por rutas de mirador
            
            **7.Utilizacion MFC**: Baja utilizacion del MFC por apertura de tienda, pero holgura en Red Friday y promociones. """)
        st.header("MFC 1000 Pedidos: Ruta Mirador")
        
        #st.header("Demanda de 100% MFC: 650 Pedidos ", )

        original_title = '<p style="color:Black; font-size: 20px;">KPIs</p>'
        st.markdown(original_title, unsafe_allow_html=True)
        
        col1, col2, col3, col4= st.columns(4)
        col1.metric("Ticket Promedio", "$45.459")
        col2.metric("% Costo de la Venta", "25,1%")
        col3.metric("Ordenes MFC", "370")
        col4.metric("Utilización MFC", "56%")



        map_sby_2 = folium.Map(location=[-33.439445474052995, -70.65461676222148], zoom_start=10)
        data_geo = json.load(open('Unimarc.geojson'))

        original_title = '<p style="color:Black; font-size: 20px;">Mapa de Santiago</p>'
        st.markdown(original_title, unsafe_allow_html=True)

        #tooltip = "MFC"
        #folium.Marker([-33.35674849571172, -70.54006548079522], popup="<i>Mt. Hood Meadows</i>", tooltip=tooltip).add_to(map_sby_2)

        tooltip = "MFC"
        folium.Marker([-33.35674849571172, -70.54006548079522], radius=2, popup="<i>Mt. Hood Meadows</i>", tooltip=tooltip, icon=folium.Icon(color='pink')).add_to(map_sby_2)


        tooltip = "Militares"
        folium.Marker([-33.403718655851755, -70.5685695153448], radius=2, popup="<i>Mt. Hood Meadows</i>", tooltip=tooltip, icon=folium.Icon(color='pink')).add_to(map_sby_2)


        tooltip = "Huechuraba"
        folium.Marker([-33.35042848321098, -70.67137054603444], radius=2, popup="<i>Mt. Hood Meadows</i>", tooltip=tooltip, icon=folium.Icon(color='pink')).add_to(map_sby_2)


        tooltip = "Leones"
        folium.Marker([-33.44840022101449, -70.59814800205135], radius=2, popup="<i>Mt. Hood Meadows</i>", tooltip=tooltip, icon=folium.Icon(color='pink')).add_to(map_sby_2)

        tooltip = "Mirador"
        folium.Marker([-33.51373958190215, -70.60675680261642], popup="<i>Mt. Hood Meadows</i>", tooltip=tooltip).add_to(map_sby_2)

        tooltip = "Silva Carvallo"
        folium.Marker([-33.532231859430375, -70.77482864554192], popup="<i>Mt. Hood Meadows</i>", tooltip=tooltip).add_to(map_sby_2)

        #tooltip = "Consistorial"
        folium.Marker([-33.48375561020082, -70.54773803862076], popup="<i>Mt. Hood Meadows</i>", tooltip=tooltip).add_to(map_sby_2)


        tooltip = "Consistorial"
        folium.Marker([-33.48375561020082, -70.54773803862076], radius=2, popup="<i>Mt. Hood Meadows</i>", tooltip=tooltip, icon=folium.Icon(color='pink')).add_to(map_sby_2)

        ### Anillo 1 
        data_geo = json.load(open('Unimarc.geojson'))
        features = []
        for x in data_geo['features']:
            if x['properties']['name'] in  ('Militares','Cordillera'):
                features.append(x)
    
        gson_anillo_1 = {'type':'FeatureCollection','features':features}
        maps= folium.Choropleth(geo_data = gson_anillo_1,
                           fill_color='green',
                           highlight=True,
                           reset=True).add_to(map_sby_2)

        ### Anillo 2
        data_geo = json.load(open('Unimarc.geojson'))
        features = []
        for x in data_geo['features']:
            if x['properties']['name'] in  ('Huechuraba','Los Leones','Consistorial'):
                features.append(x)
    
        gson_anillo_2 = {'type':'FeatureCollection','features':features}
        maps= folium.Choropleth(geo_data = gson_anillo_2,
                           fill_color='blue',
                           highlight=True,
                           reset=True).add_to(map_sby_2)
 
        
        ### Anillo 3
        data_geo = json.load(open('Unimarc.geojson'))
        features = []
        for x in data_geo['features']:
            if x['properties']['name']  == 'Mirador Norte':
                features.append(x)
    
        gson_anillo_3 = {'type':'FeatureCollection','features':features}
        maps= folium.Choropleth(geo_data = gson_anillo_3,
                           fill_color='red',
                           highlight=True,
                           reset=True).add_to(map_sby_2)

        ### Anillo 4
        data_geo = json.load(open('Unimarc.geojson'))
        features = []
        for x in data_geo['features']:
            if x['properties']['name'] in  ('Mirador Externo','Mirador Centro','Mirador Sur','Camino Nos'):
                features.append(x)
    
        gson_anillo_4 = {'type':'FeatureCollection','features':features}
        maps= folium.Choropleth(geo_data = gson_anillo_4,
                           fill_color='purple',
                           highlight=True,
                           reset=True).add_to(map_sby_2)


        ### Anillo 5
        data_geo = json.load(open('Unimarc.geojson'))
        features = []
        for x in data_geo['features']:
            if x['properties']['name'] in  ('Silva Carvallo','Mirador'):
                features.append(x)
    
        gson_anillo_5 = {'type':'FeatureCollection','features':features}
        maps= folium.Choropleth(geo_data = gson_anillo_5,
                           fill_color='gray',
                           highlight=True,
                           reset=True).add_to(map_sby_2)

        folium_static(map_sby_2)

        #df = pd.DataFrame(
        #[['Anillo Verde',1,1,1],['Verde',1,1,1]],index=pd.Index([1, 2]))

        #st.dataframe(df)

        col1, col2, col3, col4 = st.columns((1, 1, 1,1))

        #Verde
        with col1:
            original_title = '<p style="color:green; font-weight: bold; font-size: 25px;">Anillo Verde</p>'
            st.markdown(original_title, unsafe_allow_html=True)
            st.write("""**Pedidos:** 163 O/D  (16%)""")
            st.write("""**Modelo:** MFC""")
            st.write("""**Costo:** 9.280""")
            st.write("""**Costo x Orden:** 20%""")

        #Azul
        with col2:
            original_title = '<p style="color:blue; font-weight: bold; font-size: 25px;">Anillo Azul</p>'
            st.markdown(original_title, unsafe_allow_html=True)
            st.write("""**Pedidos:** 194 O/D  (19%)""")
            st.write("""**Modelo:** MFC""")
            st.write("""**Costo:** 11.020""")
            st.write("""**Costo x Orden:** 24%""")

        #Rojo
        with col3:
            original_title = '<p style="color:red; font-weight: bold; font-size: 25px;">Anillo Rojo</p>'
            st.markdown(original_title, unsafe_allow_html=True)
            st.write("""**Pedidos:** 12 O/D  (1%)""")
            st.write("""**Modelo:** MFC""")
            st.write("""**Costo:** 14.520""")
            st.write("""**Costo x Orden:** 32%""")

        #On demand
        with col4:
            original_title = '<p style="color:pink; font-weight: bold; font-size: 25px;">On-Demand</p>'
            st.markdown(original_title, unsafe_allow_html=True)
            st.write("""**Pedidos:** 129 O/D  (13%)""")
            st.write("""**Modelo:** Shopper""")
            st.write("""**Costo:** 11.318""")
            st.write("""**Costo x Orden:** 24%""")
            

        with col1:
            original_title = '<p style="color:purple; font-weight: bold; font-size: 25px;">Ruta Mirador</p>'
            st.markdown(original_title, unsafe_allow_html=True)
            st.write("""**Pedidos:** 201 O/D (21%)""")
            st.write("""**Modelo:** Picking & Ruta Mirador""")
            st.write("""**Costo:** 15.582""")
            st.write("""**Costo x Orden:** 34%""")
        
        with col2:
            original_title = '<p style="color:grey; font-weight: bold; font-size: 25px;">Shoppers</p>'
            st.markdown(original_title, unsafe_allow_html=True)
            st.write("""**Pedidos:** 301 O/D (30%)""")
            st.write("""**Modelo:** Shoppers Silva y Mirador""")
            st.write("""**Costo:** 10.038""")
            st.write("""**Costo x Orden:** 22%""")


    elif page == 'MFC 1000 Pedidos: Hub & Spoke':
        st.sidebar.write("""
            ### Consideración MFC 1000:  Hub & Spoke """)
        st.header("MFC 1000 Pedidos: Hub & Spoke")
        

        original_title = '<p style="color:Black; font-size: 20px;">KPIs</p>'
        st.markdown(original_title, unsafe_allow_html=True)
        
        col1, col2, col3, col4= st.columns(4)
        col1.metric("Ticket Promedio", "$45.459")
        col2.metric("% Costo de la Venta", "24%")
        col3.metric("Ordenes MFC", "564")
        col4.metric("Utilización MFC", "86%")



        map_sby_3 = folium.Map(location=[-33.439445474052995, -70.65461676222148], zoom_start=10)
        data_geo = json.load(open('Unimarc.geojson'))

        original_title = '<p style="color:Black; font-size: 20px;">Mapa de Santiago</p>'
        st.markdown(original_title, unsafe_allow_html=True)

        tooltip = "MFC"
        folium.Marker([-33.35674849571172, -70.54006548079522], radius=2, popup="<i>Mt. Hood Meadows</i>", tooltip=tooltip, icon=folium.Icon(color='pink')).add_to(map_sby_3)
 

        tooltip = "Militares"
        folium.Marker([-33.403718655851755, -70.5685695153448], radius=2, popup="<i>Mt. Hood Meadows</i>", tooltip=tooltip, icon=folium.Icon(color='pink')).add_to(map_sby_3)


        tooltip = "Huechuraba"
        folium.Marker([-33.35042848321098, -70.67137054603444], radius=2, popup="<i>Mt. Hood Meadows</i>", tooltip=tooltip, icon=folium.Icon(color='pink')).add_to(map_sby_3)


        tooltip = "Leones"
        folium.Marker([-33.44840022101449, -70.59814800205135], radius=2, popup="<i>Mt. Hood Meadows</i>", tooltip=tooltip, icon=folium.Icon(color='pink')).add_to(map_sby_3)

        tooltip = "Mirador"
        folium.Marker([-33.51373958190215, -70.60675680261642], popup="<i>Mt. Hood Meadows</i>", tooltip=tooltip).add_to(map_sby_3)

        tooltip = "Silva Carvallo"
        folium.Marker([-33.532231859430375, -70.77482864554192], popup="<i>Mt. Hood Meadows</i>", tooltip=tooltip).add_to(map_sby_3)

        tooltip = "Consistorial"
        folium.Marker([-33.48375561020082, -70.54773803862076], popup="<i>Mt. Hood Meadows</i>", tooltip=tooltip).add_to(map_sby_3)


        tooltip = "Consistorial"
        folium.Marker([-33.48375561020082, -70.54773803862076], radius=2, popup="<i>Mt. Hood Meadows</i>", tooltip=tooltip, icon=folium.Icon(color='pink')).add_to(map_sby_3)


        ### Anillo 1 
        data_geo = json.load(open('Unimarc.geojson'))
        features = []
        for x in data_geo['features']:
            if x['properties']['name'] in  ('Militares','Cordillera'):
                features.append(x)
    
        gson_anillo_1 = {'type':'FeatureCollection','features':features}
        maps= folium.Choropleth(geo_data = gson_anillo_1,
                           fill_color='green',
                           highlight=True,
                           reset=True).add_to(map_sby_3)

        ### Anillo 2
        data_geo = json.load(open('Unimarc.geojson'))
        features = []
        for x in data_geo['features']:
            if x['properties']['name'] in  ('Huechuraba','Los Leones','Consistorial'):
                features.append(x)
    
        gson_anillo_2 = {'type':'FeatureCollection','features':features}
        maps= folium.Choropleth(geo_data = gson_anillo_2,
                           fill_color='blue',
                           highlight=True,
                           reset=True).add_to(map_sby_3)
 
        
        ### Anillo 3
        data_geo = json.load(open('Unimarc.geojson'))
        features = []
        for x in data_geo['features']:
            if x['properties']['name']  == 'Mirador Norte':
                features.append(x)
    
        gson_anillo_3 = {'type':'FeatureCollection','features':features}
        maps= folium.Choropleth(geo_data = gson_anillo_3,
                           fill_color='red',
                           highlight=True,
                           reset=True).add_to(map_sby_3)

        ### Anillo 4
        data_geo = json.load(open('Unimarc.geojson'))
        features = []
        for x in data_geo['features']:
            if x['properties']['name'] in  ('Mirador Externo','Mirador Centro','Mirador Sur','Camino Nos'):
                features.append(x)
    
        gson_anillo_4 = {'type':'FeatureCollection','features':features}
        maps= folium.Choropleth(geo_data = gson_anillo_4,
                           fill_color='purple',
                           highlight=True,
                           reset=True).add_to(map_sby_3)


        ### Anillo 5
        data_geo = json.load(open('Unimarc.geojson'))
        features = []
        for x in data_geo['features']:
            if x['properties']['name'] in  ('Silva Carvallo','Mirador'):
                features.append(x)
    
        gson_anillo_5 = {'type':'FeatureCollection','features':features}
        maps= folium.Choropleth(geo_data = gson_anillo_5,
                           fill_color='gray',
                           highlight=True,
                           reset=True).add_to(map_sby_3)

        folium_static(map_sby_3)


        col1, col2, col3,col4 = st.columns((1,1,1,1))

        #Verde
        with col1:
            original_title = '<p style="color:green; font-weight: bold; font-size: 25px;">Anillo Verde</p>'
            st.markdown(original_title, unsafe_allow_html=True)
            st.write("""**Pedidos:** 163 O/D  (16%)""")
            st.write("""**Modelo:** MFC""")
            st.write("""**Costo:** 9.280""")
            st.write("""**Costo x Orden:** 20%""")

        #Azul
        with col2:
            original_title = '<p style="color:blue; font-weight: bold; font-size: 25px;">Anillo Azul</p>'
            st.markdown(original_title, unsafe_allow_html=True)
            st.write("""**Pedidos:** 194 O/D  (19%)""")
            st.write("""**Modelo:** MFC""")
            st.write("""**Costo:** 11.020""")
            st.write("""**Costo x Orden:** 24%""")

        #Rojo
        with col3:
            original_title = '<p style="color:red; font-weight: bold; font-size: 25px;">Anillo Rojo</p>'
            st.markdown(original_title, unsafe_allow_html=True)
            st.write("""**Pedidos:** 12 O/D  (1%)""")
            st.write("""**Modelo:** MFC""")
            st.write("""**Costo:** 14.520""")
            st.write("""**Costo x Orden:** 32%""")

        #On demand
        with col4:
            original_title = '<p style="color:pink; font-weight: bold; font-size: 25px;">On-Demand</p>'
            st.markdown(original_title, unsafe_allow_html=True)
            st.write("""**Pedidos:** 129 O/D  (13%)""")
            st.write("""**Modelo:** Shopper""")
            st.write("""**Costo:** 11.318""")
            st.write("""**Costo x Orden:** 24%""")

        with col1:
            original_title = '<p style="color:purple; font-weight: bold; font-size: 25px;">Hub & Spoke </p>'
            st.markdown(original_title, unsafe_allow_html=True)
            st.write("""**Pedidos:** 201 O/D (21%)""")
            st.write("""**Modelo:** MFC Hub & Spoke""")
            st.write("""**Costo:** 12.880""")
            st.write("""**Costo x Orden:** 28%""")
            st.write("""**Costo Actual:** 34%""")

        with col2:
            original_title = '<p style="color:grey; font-weight: bold; font-size: 25px;">Shoppers</p>'
            st.markdown(original_title, unsafe_allow_html=True)
            st.write("""**Pedidos:** 301 O/D (30%)""")
            st.write("""**Modelo:** Shoppers Silva y Mirador""")
            st.write("""**Costo:** 10.038""")
            st.write("""**Costo x Orden:** 22%""")

        


    if page == 'MFC 2000 Pedidos':
        st.sidebar.write("""
            ### Consideración MFC con 2000 pedidos""")
        st.header("MFC 2000 Pedidos: MFC2 o nuevas tiendas")
        

        original_title = '<p style="color:Black; font-size: 20px;">KPIs</p>'
        st.markdown(original_title, unsafe_allow_html=True)
        
        col1, col2, col3, col4= st.columns(4)
        col1.metric("Ticket Promedio", "$45.459")
        col2.metric("% Costo de la Venta", "24,7%")
        col3.metric("Ordenes MFC", "646")
        col4.metric("Utilización MFC", "99%")



        map_sby_4 = folium.Map(location=[-33.439445474052995, -70.65461676222148], zoom_start=10)
        data_geo = json.load(open('Unimarc.geojson'))

        original_title = '<p style="color:Black; font-size: 20px;">Mapa de Santiago</p>'
        st.markdown(original_title, unsafe_allow_html=True)

        tooltip = "MFC"
        folium.Marker([-33.35674849571172, -70.54006548079522], radius=2, popup="<i>Mt. Hood Meadows</i>", tooltip=tooltip, icon=folium.Icon(color='pink')).add_to(map_sby_4)
      

        tooltip = "Militares"
        folium.Marker([-33.403718655851755, -70.5685695153448], radius=2, popup="<i>Mt. Hood Meadows</i>", tooltip=tooltip, icon=folium.Icon(color='pink')).add_to(map_sby_4)


        tooltip = "Huechuraba"
        folium.Marker([-33.35042848321098, -70.67137054603444], radius=2, popup="<i>Mt. Hood Meadows</i>", tooltip=tooltip, icon=folium.Icon(color='pink')).add_to(map_sby_4)


        tooltip = "Leones"
        folium.Marker([-33.44840022101449, -70.59814800205135], radius=2, popup="<i>Mt. Hood Meadows</i>", tooltip=tooltip, icon=folium.Icon(color='pink')).add_to(map_sby_4)

        tooltip = "Mirador"
        folium.Marker([-33.51373958190215, -70.60675680261642], popup="<i>Mt. Hood Meadows</i>", tooltip=tooltip).add_to(map_sby_4)

        tooltip = "Silva Carvallo"
        folium.Marker([-33.532231859430375, -70.77482864554192], popup="<i>Mt. Hood Meadows</i>", tooltip=tooltip).add_to(map_sby_4)

        tooltip = "Consistorial"
        folium.Marker([-33.48375561020082, -70.54773803862076], popup="<i>Mt. Hood Meadows</i>", tooltip=tooltip).add_to(map_sby_4)



        ### Anillo 1 
        data_geo = json.load(open('Unimarc.geojson'))
        features = []
        for x in data_geo['features']:
            if x['properties']['name'] in  ('Militares','Cordillera'):
                features.append(x)
    
        gson_anillo_1 = {'type':'FeatureCollection','features':features}
        maps= folium.Choropleth(geo_data = gson_anillo_1,
                           fill_color='green',
                           highlight=True,
                           reset=True).add_to(map_sby_4)

        ### Anillo 2
        data_geo = json.load(open('Unimarc.geojson'))
        features = []
        for x in data_geo['features']:
            if x['properties']['name'] in  ('Huechuraba','Los Leones'):
                features.append(x)
    
        gson_anillo_2 = {'type':'FeatureCollection','features':features}
        maps= folium.Choropleth(geo_data = gson_anillo_2,
                           fill_color='blue',
                           highlight=True,
                           reset=True).add_to(map_sby_4)
 
        
        ### Anillo 3
        data_geo = json.load(open('Unimarc.geojson'))
        features = []
        for x in data_geo['features']:
            if x['properties']['name']  == 'Mirador Norte':
                features.append(x)
        gson_anillo_3 = {'type':'FeatureCollection','features':features}
        maps= folium.Choropleth(geo_data = gson_anillo_3,
                           fill_color='red',
                           highlight=True,
                           reset=True).add_to(map_sby_4)

        ### Anillo 4
        data_geo = json.load(open('Unimarc.geojson'))
        features = []
        for x in data_geo['features']:
            if x['properties']['name'] in  ('Mirador Externo','Mirador Centro','Mirador Sur','Camino Nos'):
                features.append(x)
    
        gson_anillo_4 = {'type':'FeatureCollection','features':features}
        maps= folium.Choropleth(geo_data = gson_anillo_4,
                           fill_color='purple',
                           highlight=True,
                           reset=True).add_to(map_sby_4)


        ### Anillo 5
        data_geo = json.load(open('Unimarc.geojson'))
        features = []
        for x in data_geo['features']:
            if x['properties']['name'] in  ('Silva Carvallo','Consistorial','Mirador'):
                features.append(x)
    
        gson_anillo_5 = {'type':'FeatureCollection','features':features}
        maps= folium.Choropleth(geo_data = gson_anillo_5,
                           fill_color='gray',
                           highlight=True,
                           reset=True).add_to(map_sby_4)

        folium_static(map_sby_4)

        col1, col2, col3,col4 = st.columns((1,1,1,1))

        #Verde
        with col1:
            original_title = '<p style="color:green; font-weight: bold; font-size: 25px;">Anillo Verde</p>'
            st.markdown(original_title, unsafe_allow_html=True)
            st.write("""**Pedidos:** 300 O/D  (15%)""")
            st.write("""**Modelo:** MFC""")
            st.write("""**Costo:** 9.280""")
            st.write("""**Costo x Orden:** 20%""")

        #Azul
        with col2:
            original_title = '<p style="color:blue; font-weight: bold; font-size: 25px;">Anillo Azul</p>'
            st.markdown(original_title, unsafe_allow_html=True)
            st.write("""**Pedidos:** 300 O/D  (15%)""")
            st.write("""**Modelo:** MFC""")
            st.write("""**Costo:** 11.020""")
            st.write("""**Costo x Orden:** 24%""")

        #Rojo
        with col3:
            original_title = '<p style="color:red; font-weight: bold; font-size: 25px;">Anillo Rojo</p>'
            st.markdown(original_title, unsafe_allow_html=True)
            st.write("""**Pedidos:** 24 O/D  (1%)""")
            st.write("""**Modelo:** MFC""")
            st.write("""**Costo:** 14.520""")
            st.write("""**Costo x Orden:** 32%""")

        #On demand
        with col4:
            original_title = '<p style="color:pink; font-weight: bold; font-size: 25px;">On-Demand</p>'
            st.markdown(original_title, unsafe_allow_html=True)
            st.write("""**Pedidos:** 260 O/D  (13%)""")
            st.write("""**Modelo:** Shopper""")
            st.write("""**Costo:** 12.050""")
            st.write("""**Costo x Orden:** 27%""")

        with col1:
            original_title = '<p style="color:purple; font-weight: bold; font-size: 25px;">Ruta Mirador </p>'
            st.markdown(original_title, unsafe_allow_html=True)
            st.write("""**Pedidos:** 393 O/D (19%)""")
            st.write("""**Modelo:** Picking & Ruta Mirador""")
            st.write("""**Costo:** 12.880""")
            st.write("""**Costo x Orden:** 28%""")
            st.write("""**Costo Actual:** 34%""")

        with col2:
            original_title = '<p style="color:grey; font-weight: bold; font-size: 25px;">Shoppers</p>'
            st.markdown(original_title, unsafe_allow_html=True)
            st.write("""**Pedidos:** 723 O/D (36%)""")
            st.write("""**Modelo:** Shoppers Silva, Mirador y Consistorial""")
            st.write("""**Costo:** 9.995""")
            st.write("""**Costo x Orden:** 22%""")

 
run_UI()
