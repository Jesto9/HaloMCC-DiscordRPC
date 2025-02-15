import json

def jsonDictionary(dictionary):
    haloreachdictionary = {
        "Easy" : "a_easy",
        "Normal" : "a_normal",
        "Heroic" : "a_heroic",
        "Legendary" : "a_legendary",
        "HaloReach": "a_logo",
        "Anchor 9": "anchor9",
        "Battle Canyon": "battlecanyon",
        "Beachhead": "beachhead",
        "Boardwalk": "boardwalk",
        "Boneyard": "boneyard",
        "Breakneck": "breakneck",
        "Breakpoint": "breakpoint",
        "Carteglacier": "carteglacier",
        "Coastline": "coastline",
        "Condemned": "condemned",
        "Corvette": "corvette",
        "Countdown": "countdown",
        "Courtyard": "courtyard",
        "Damnation": "damnation",
        "Hang 'Em High": "hangemhigh",
        "Highlands": "highlands",
        "Holdout": "holdout",
        "Installation 04": "installation04",
        "Overlook": "overlook",
        "Powerhouse": "powerhouse",
        "Reach Water Front": "reachwaterfront",
        "Reflection": "reflection",
        "Ridgeline": "ridgeline",
        "Solitary": "solitary",
        "Spire": "spire",
        "Swordbase": "swordbase",
        "Tempest": "tempest",
        "Unearthed": "unearthed",
        "Zealot": "zealot"
    }
    halocedictionary = {
        "Easy" : "a_easy",
        "Normal" : "a_normal",
        "Heroic" : "a_heroic",
        "Legendary" : "a_legendary",
        "HaloCE" : "a_logo",
        "Battle Creek" : "battlecreek",
        "Sidewinder" : "sidewinder",
        "Damnation" : "damnation",
        "Rat Race" : "ratrace",
        "Prisoner" : "prisoner",
        "Hang 'Em High" : "hangemhigh",
        "Chill Out" : "chillout",
        "Derelict" : "derelict",
        "Boarding Action" : "boardingaction",
        "Chiron TL-34" : "chirontl-34",
        "Bloodgulch" : "bloodgulch",
        "Wizard" : "wizard",
        "Longest" : "longest",
        "Death Island" : "deathisland",
        "Danger Canyon" : "dangercanyon",
        "Infinity" : "infinity",
        "Timberland" : "timberland",
        "Icefield" : "icefield",
        "Gephyrophobia" : "gephyrophobia"    
    }
    halo2dictionary = {
        "Easy": "a_easy", 
        "Heroic": "a_heroic",
        "Legendary": "a_legendary",
        "Normal": "a_normal",
        "Halo2Anniversary": {
            "Halo2A": "a_logo",
            "Awash": "b_awash",
            "Bloodline": "b_bloodline",
            "Lockdown": "b_lockdown",
            "Nebula": "b_nebula",
            "Remnant": "b_remnant",
            "Shrine": "b_shrine",
            "Skyward": "b_skyward",
            "Stonetown": "b_stonetown",
            "Warlord": "b_warlord", 
            "Zenith": "b_zenith"
        },
        "Halo2Classic": {
            "Halo2": "ab_logo",
            "Lockout": "lockout",
            "Ascension": "ascension",
            "Midship": "midship",
            "Ivory Tower": "ivorytower",
            "Beaver Creek": "beavercreek",
            "Burial Mounds": "burialmounds",
            "Colossus": "colossus",
            "Zanzibar": "zanzibar",
            "Coagulation": "coagulation",
            "Headlong": "headlong",
            "Waterworks": "waterworks",
            "Foundation": "foundation",
            "Containment": "containment",
            "Warlock": "warlock",
            "Sanctuary": "sanctuary",
            "Turf": "turf",
            "Backwash": "backwash",
            "Elongation": "elongation",
            "Gemini": "gemini",
            "Relic": "relic",
            "Terminal": "terminal",
            "Desolation": "desolation",
            "Tombstone": "tombstone",
            "District": "district",
            "Uplift": "uplift",
        }
    }

    halo3dictionary = {
        "Easy" : "a_easy",
        "Normal" : "a_normal" ,   
        "Heroic" : "a_heroic",
        "Legendary" : "a_legendary",
        "ODST" : "a_logo",
        "Halo3" : "a_logo1",
        "Assembly" : "assembly",
        "Avalanche" : "avalanche",
        "Blackout" : "blackout",
        "Citadel" : "citadel",
        "Cold Storage" : "cold_storage",
        "Construct" : "construct",
        "Epitaph" : "epitaph",
        "Foundry" : "foundry",
        "Ghost Town" : "ghost_town",
        "Guardian" : "guardian",
        "Heretic" : "heretic",
        "High Ground" : "high_ground",
        "Isolation" : "isolation",
        "Last Resort" : "last_resort",
        "Longshore" : "longshore",
        "Narrows" : "narrows",
        "Orbital" : "orbital",
        "Rat's nest" : "rat_s_nest",
        "Sandbox" : "sandbox",
        "Sandtrap" : "sandtrap",
        "Snowbound" : "snowbound",
        "Standoff" : "standoff",
        "Valhalla" : "valhalla"
    }

    halo4dictionary = {
        "Easy" : "a_easy",
        "Normal" : "a_normal",
        "Heroic" : "a_heroic",
        "Legendary" : "a_legendary",
        "Halo4" : "a_logo",
        "Abandon" : "abandon",
        "Adrift" : "adrift",
        "Complex" : "complex",
        "Daybreak" : "daybreak",
        "Erosion" : "erosion",
        "Exile" : "exile",
        "Forge Island" : "forge_island",
        "Harvest" : "harvest",
        "Haven" : "haven",
        "Impact" : "impact",
        "Landfall" : "landfall",
        "Longbow" : "longbow",
        "Meltdown" : "meltdown",
        "Monolith" : "monolith",
        "Outcast" : "outcast",
        "Perdition" : "perdition",
        "Pitfall" : "pitfall",
        "Ragnarok" : "ragnarok",
        "Ravine" : "ravine",
        "Shatter" : "shatter",
        "Skyline" : "skyline",
        "Solace" : "solace",
        "Vertigo" : "vertigo",
        "Vortex" : "vortex",
        "Wreckage" : "wreckage"
    }
    if(dictionary == 0):
        return haloreachdictionary
    elif(dictionary == 1):
        return halocedictionary
    elif(dictionary == 2):
        return halo2dictionary
    elif(dictionary == 3):
        return halo3dictionary
    elif(dictionary == 4):
        return halo4dictionary


if __name__ == '__main__':
    print(json.dumps(jsonDictionary(3), indent=2))
