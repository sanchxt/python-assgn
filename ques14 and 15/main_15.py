class Password:
    def __init__(self, file_path):
        self.file_path = file_path

    def create_csv(self):
        with open(self.file_path, 'w') as file:
            file.write('user_id,password\n')

            while True:
                user_id = input('User ID (exit to finish): ')
                if user_id.lower() == 'exit':
                    break
                password = input('Password: ')

                file.write(f'{user_id},{password}\n')

    def search_pw(self, user_id):
        with open(self.file_path, 'r') as file:
            lines = file.readlines()
            header, *data = lines

            for line in data:
                curr_user, curr_pw = line.strip().split(',')
                if curr_user == user_id:
                    print(f'password: {curr_pw}')
                    return
            print(f'{user_id} not found')


if __name__ == '__main__':
    file_path = 'assignments/ques15/passwords.csv'
    pw_mgr = Password(file_path)

    pw_mgr.create_csv()

    search_id = input('Enter User ID to search for: ')
    pw_mgr.search_pw(search_id)
