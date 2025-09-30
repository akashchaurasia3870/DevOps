def get_data():
    with open('data.txt') as f:
        data = f.read()
        data = data.split()
        return data
        # for i,val in enumerate(data):
        #     print(f"{i+1} {val}")

