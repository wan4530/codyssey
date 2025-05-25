import random

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
        
if __name__ == "__main__":
    #DummySensor 인스턴스 만들기
    ds = DummySensor()
    #값 설정하기
    ds.set_env()
    #값들을 가져오고 출력하기
    env = ds.get_env()
    for k,v in env.items():
        print('%-30s : %9.5f' %(k,v))
