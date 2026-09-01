def solution_station_5():
    
    # Create dictionary for LT
    lt_groups = {
        1: ["Ainas", "Tobit", "Yasmin", "Zoe", "Iuliia", "Klementyna", "Markus", "Mufang", 
            "Oumaima", "Ebony", "Nandini", "Nathan", "Tiara", "Yurui", "Ben", 
            "Christopher", "Lula", "Muni", "Yuvraj"],
        2: ["Huy Bao", "Iris", "Katharina", "Minseo", "Sade", "Alex", "Arwen", 
            "Rajko", "Sylwia", "Zeno", "Christina", "Helen", "Mark", "Mats", 
            "Vadim", "David", "Lora", "Quinn", "Tarling"],
        3: ["Elizabethe", "Gabriel", "Jakub", "Luc", "Soelie", "Aleksandra", "Arnav", "Donna", 
            "Milan", "Ronze", "Cris", "Jingqi", "Oliver", "Vaayu", "Yusef", "Afua", 
            "Anna", "Daniel", "Nataly", "Rafael"],
        4: ["Jeremy", "Krishiv", "Neel", "Yujie", "Yutong", "An", "Heer", 
            "Paige", "Samir", "Amalia", "Douwe", "Illya", "Maria", "Rakin", 
            "Lara", "Lucas", "Michelle", "Oliwia", "Tom"],
    }

    # Reverse the mapping- name input returns number output
    name_to_lt = {n: lt for lt, names in lt_groups.items() for n in names}

    # Return LT number
    return name_to_lt.get(name, -1)