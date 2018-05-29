from src.Repository import Repository

temperature_filename = "../data/temperature.dat"

if __name__ == '__main__':
    temperature_repository = Repository(temperature_filename)

    print(len(temperature_repository.data))
