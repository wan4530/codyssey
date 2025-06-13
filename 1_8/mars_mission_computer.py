import random
import platform  # 운영체제 정보를 가져오기 위한 모듈
import os  # CPU 코어 수를 가져오기 위한 모듈
import psutil  # 메모리, CPU 사용량을 가져오기 위한 모듈

class DummySensor:
    env_values = {
        'mars_base_internal_temperature' : 0.0,
        'mars_base_external_temperature' : 0.0,
        'mars_base_internal_humidity' : 0.0,
        'mars_base_external_illuminance' : 0.0,
        'mars_base_internal_co2' : 0.0,
        'mars_base_internal_oxygen' : 0.0
    }
    def get_env(self):
        return DummySensor.env_values
    def set_env(self):
        
        DummySensor.env_values['mars_base_internal_temperature'] = random.uniform(18, 30)
        DummySensor.env_values['mars_base_external_temperature'] = random.uniform(0,21)
        DummySensor.env_values['mars_base_internal_humidity'] = random.uniform(50, 60)
        DummySensor.env_values['mars_base_external_illuminance'] = random.uniform(500, 715)
        DummySensor.env_values['mars_base_internal_co2'] = random.uniform(0.02,0.1)
        DummySensor.env_values['mars_base_internal_oxygen'] = random.uniform(4,7)

class MissionComputer:
    env_values = {
        "mars_base_internal_temperature": 0.0,
        "mars_base_external_temperature": 0.0,
        "mars_base_internal_humidity": 0.0,
        "mars_base_external_illuminance": 0.0,
        "mars_base_internal_co2": 0.0,
        "mars_base_internal_oxygen": 0.0
    }
    
    def get_sensor_data(self):
        ds = DummySensor()
        ds.set_env()
        #센서의 값을 가져와서 env_values에 담기
        envs = ds.get_env()
        
        MissionComputer.env_values["mars_base_internal_temperature"] = envs["mars_base_internal_temperature"]
        MissionComputer.env_values["mars_base_external_temperature"] = envs["mars_base_external_temperature"]
        MissionComputer.env_values["mars_base_internal_humidity"] = envs["mars_base_internal_humidity"]
        MissionComputer.env_values["mars_base_external_illuminance"] = envs["mars_base_external_illuminance"]
        MissionComputer.env_values["mars_base_internal_co2"] = envs["mars_base_internal_co2"]
        MissionComputer.env_values["mars_base_internal_oxygen"] = envs["mars_base_internal_oxygen"]
        
        #json 형태로 env_values 출력
        values = list(MissionComputer.env_values.items())
        print("{")
        for k, v in values:
                if(k == values[-1][0]):
                    print(f"    \"{k}\" : {v}")
                
                else:
                    print(f"    \"{k}\" : {v},")
        print("}")
    def get_mission_computer_info(self):
        system_info = {
            'operating_system': platform.system(),  # 운영체계
            'os_version': platform.version(),  # 운영체계 버전
            'cpu_type': platform.processor(),  # CPU 타입
            'cpu_core_count': os.cpu_count(),  # CPU 코어 수
            'memory_size': f"{round(psutil.virtual_memory().total / (1024 ** 3), 2)} GB"  # 메모리 크기
        }
        # JSON 형식으로 출력
        print("{")
        items = list(system_info.items())
        for i, (k, v) in enumerate(items):
                if(i < len(items)-1):
                    print(f"    \"{k}\" : {v}")
                else:
                    print(f"    \"{k}\" : {v},")
        print("}")

    def get_mission_computer_load(self):
        load_info = {
            'cpu_usage_percent': psutil.cpu_percent(interval=1),  # CPU 사용량
            'memory_usage_percent': psutil.virtual_memory().percent  # 메모리 사용량
        }
        # JSON 형식으로 출력
        items = list(load_info.items())
        for i, (k, v) in enumerate(items):
                if(i < len(items)-1):
                    print(f"    \"{k}\" : {v}")
                else:
                    print(f"    \"{k}\" : {v},")
        print("}")

# MissionComputer 인스턴스 생성
runComputer = MissionComputer()

# 시스템 정보 출력
runComputer.get_mission_computer_info()

runComputer.get_mission_computer_load()
