# Platform Generator Class
# Entirely written by humans with assistance from Copilot (75% human, 25% AI)

import random
from utils.platform import Platform


class PlatformGenerator():
    def randWidth():
        widths = [Platform.WIDTH_THIN, Platform.WIDTH_NORMAL, Platform.WIDTH_THICK]
        return random.choice(widths)
    
    def randFloorType():
        types = [Platform.TYPE_GRASS, Platform.TYPE_ICE]
        return random.choice(types)

    def randEffectType():
        random_num = random.random();
        if random_num > 0.95:
            return Platform.TYPE_BOOST
        if random_num > 0.80:
            return Platform.TYPE_SPIKE
        else:
            return None

    def gen3Plat():
        has_effect = False

        plat1_width = PlatformGenerator.randWidth()
        plat1_type = PlatformGenerator.randFloorType()
        plat1_effect = PlatformGenerator.randEffectType()
        if plat1_effect != None:
            has_effect = True
        
        plat1 = Platform(0, 0, plat1_type, plat1_width, 0)

        plat2_width = PlatformGenerator.randWidth()
        plat2_type = 1
        plat2_effect = None
        if not has_effect:
            plat2_effect = PlatformGenerator.randEffectType()
        if plat2_effect != None:
            has_effect = True
        
        plat2 = Platform(400 - ((plat2_width * 80) / 2), 0, plat2_type, plat2_width, 0)
        
        plat3_width = PlatformGenerator.randWidth()
        plat3_type = PlatformGenerator.randFloorType()
        plat3_effect = None
        if not has_effect:
            plat3_effect = PlatformGenerator.randEffectType()
        
        plat3 = Platform(800 - (plat3_width * 80), 0, plat3_type, plat3_width, 0)
        
        return [plat1, plat2, plat3]

    def gen2Plat():
        has_effect = False

        plat1_width = PlatformGenerator.randWidth()
        plat1_type = PlatformGenerator.randFloorType()
        plat1_effect = PlatformGenerator.randEffectType()
        if plat1_effect != None:
            has_effect = True
        
        plat1 = Platform(200 - ((plat1_width * 80) / 2), 0, plat1_type, plat1_width, 0)

        plat2_width = PlatformGenerator.randWidth()
        plat2_type = PlatformGenerator.randFloorType()
        plat2_effect = None
        if not has_effect:
            plat2_effect = PlatformGenerator.randEffectType()
        
        plat2 = Platform(600 - ((plat2_width * 80) / 2), 0, plat2_type, plat2_width, 0)
        
        return [plat1, plat2]

    def gen1Plat():
        plat_width = PlatformGenerator.randWidth()
        plat_type = PlatformGenerator.randFloorType()

        plat1 = Platform(0, 0, plat_type, plat_width, 0)
        plat2 = Platform(400 - ((plat_width * 80) / 2), 0, plat_type, plat_width, 0)
        plat3 = Platform(800 - (plat_width * 80), 0, plat_type, plat_width, 0)

        platforms = [plat1, plat2, plat3]
        return [random.choice(platforms)]

    def genMovingPlat():
        plat_width = PlatformGenerator.randWidth()
        plat_type = PlatformGenerator.randFloorType()

        plat1 = Platform(0, 0, plat_type, plat_width, 2)
        plat2 = Platform(400 - ((plat_width * 80) / 2), 0, plat_type, plat_width, 2)
        plat3 = Platform(800 - (plat_width * 80), 0, plat_type, plat_width, -2)

        platforms = [plat1, plat2, plat3]
        return [random.choice(platforms)]
    
    def getPlatforms():
        generators = [PlatformGenerator.gen1Plat, PlatformGenerator.gen2Plat, PlatformGenerator.gen3Plat, PlatformGenerator.genMovingPlat]
        return random.choice(generators)()
