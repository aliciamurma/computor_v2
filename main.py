def ft_check_statement(statement):
    if (statement.find("=") != -1)
        print("Error in synthaxis")
        sys.exit(-1)

def ft_is_variable(var):
    var2 = var.split('=')


def ft_process_statement(statement):
    ft_check_statement(statement);
    if (ft_is_variable(statement)):
        ft_save_variable(statement)

def ft_start():
    prompt = getenv("Enter an statement")
    while prompt is None or prompt == '':
        prompt = 'Enter an statement: '
    while True:
        statement = input(prompt)
        ft_process_statement(statement)

def main():
    try:
        if len(argv) == 1:
            ft_start()
    except error as e:
        print("Error\n", e);

if __name__ == '__main__':
	main()
