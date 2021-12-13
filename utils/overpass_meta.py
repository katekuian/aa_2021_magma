def get_meta_data():
    return {
        "sustenance": {
            "filepath": "../00_data/sustenance_pois.json",
            "query": """
                [out:json]; 
                area[name = "Los Angeles"]->.a;
                area[name = "Santa Monica"]->.b; 
                area[name = "Burbank"]->.c; 
                (   
                    node(area.a)[amenity=bar];
                    node(area.a)[amenity=restaurant]; 
                    node(area.a)[amenity=pub];
                    node(area.a)[amenity=ice_cream];
                    node(area.a)[amenity=food_court];
                    node(area.a)[amenity=fast_food];
                    node(area.a)[amenity=biergarten];
                    node(area.a)[amenity=cafe];
                    
                    node(area.b)[amenity=bar];
                    node(area.b)[amenity=restaurant]; 
                    node(area.b)[amenity=pub];
                    node(area.b)[amenity=ice_cream];
                    node(area.b)[amenity=food_court];
                    node(area.b)[amenity=fast_food];
                    node(area.b)[amenity=biergarten];
                    node(area.b)[amenity=cafe];

                    node(area.c)[amenity=bar];
                    node(area.c)[amenity=restaurant]; 
                    node(area.c)[amenity=pub];
                    node(area.c)[amenity=ice_cream];
                    node(area.c)[amenity=food_court];
                    node(area.c)[amenity=fast_food];
                    node(area.c)[amenity=biergarten];
                    node(area.c)[amenity=cafe]; 
                ); 
                out;  
            """,
        },
        "public_transport": {
            "filepath": "../00_data/public_transport_pois.json",
            "query": """ [out:json]; 
                area[name = "Los Angeles"]->.a;
                area[name = "Santa Monica"]->.b; 
                area[name = "Burbank"]->.c; 
                (   
                    node(area.a)[public_transport=station];
                    node(area.b)[public_transport=station];
                    node(area.c)[public_transport=station];

                    node(area.a)[public_transport=platform];
                    node(area.b)[public_transport=platform];
                    node(area.c)[public_transport=platform];

                    node(area.a)[public_transport=stop_position];
                    node(area.b)[public_transport=stop_position];
                    node(area.c)[public_transport=stop_position];
                ); 
                out; """,
        },
        "education": {
            "filepath": "../00_data/education_pois.json",
            "query": """ [out:json]; 
                area[name = "Los Angeles"]->.a;
                area[name = "Santa Monica"]->.b; 
                area[name = "Burbank"]->.c; 
                (   
                    node(area.a)[amenity=college];
                    node(area.b)[amenity=college];
                    node(area.c)[amenity=college];

                    node(area.a)[amenity=library];
                    node(area.b)[amenity=library];
                    node(area.c)[amenity=library];
                
                    node(area.a)[amenity=driving_school];
                    node(area.b)[amenity=driving_school];
                    node(area.c)[amenity=driving_school];
                
                    node(area.a)[amenity=language_school];
                    node(area.b)[amenity=language_school];
                    node(area.c)[amenity=language_school];
                
                    node(area.a)[amenity=music_school];
                    node(area.b)[amenity=music_school];
                    node(area.c)[amenity=music_school];
                
                    node(area.a)[amenity=school];
                    node(area.b)[amenity=school];
                    node(area.c)[amenity=school];
                
                    node(area.a)[amenity=university];
                    node(area.b)[amenity=university];
                    node(area.c)[amenity=university];
                ); 
                out; """,
        },
        "arts_and_culture": {
            "filepath": "../00_data/arts_and_culture_pois.json",
            "query": """ [out:json]; 
                area[name = "Los Angeles"]->.a;
                area[name = "Santa Monica"]->.b; 
                area[name = "Burbank"]->.c; 
                (   
                    node(area.a)[amenity=arts_centre];
                    node(area.b)[amenity=arts_centre];
                    node(area.c)[amenity=arts_centre];

                    node(area.a)[amenity=theatre];
                    node(area.b)[amenity=theatre];
                    node(area.c)[amenity=theatre];
                
                    node(area.a)[amenity=cinema];
                    node(area.b)[amenity=cinema];
                    node(area.c)[amenity=cinema];
                ); 
                out;""",
        },
        "sports": {
            "filepath": "../00_data/sports.json",
            "query": """[out:json]; 
                area[name = "Los Angeles"]->.a;
                area[name = "Santa Monica"]->.b; 
                area[name = "Burbank"]->.c; 
                (
                    node(area.a)[leisure=fitness_station];
                    node(area.b)[leisure=fitness_station];
                    node(area.c)[leisure=fitness_station];
                
                    node(area.a)[leisure=fitness_centre];
                    node(area.b)[leisure=fitness_centre];
                    node(area.c)[leisure=fitness_centre];
                
                    node(area.a)[leisure=sports_centre];
                    node(area.b)[leisure=sports_centre];
                    node(area.c)[leisure=sports_centre];
                
                    node(area.a)[leisure=swimming_area];
                    node(area.b)[leisure=swimming_area];
                    node(area.c)[leisure=swimming_area];
                
                    node(area.a)[leisure=swimming_pool];
                    node(area.b)[leisure=swimming_pool];
                    node(area.c)[leisure=swimming_pool];

                ); 
                out;""",
        },
    }
