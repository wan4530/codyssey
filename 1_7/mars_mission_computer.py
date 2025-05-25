import p1_6.mars_mission_computer
import time

ds = p1_6.mars_mission_computer.DummySensor()

#MissionComputer class 생성
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
        while True:
            
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
            #5초 기다리기기
            time.sleep(5)


RunComputer = MissionComputer()
RunComputer.get_sensor_data()