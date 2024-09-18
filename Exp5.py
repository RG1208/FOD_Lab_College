def read_and_write_file(input_file, output_file):
    try:
        
        with open(input_file, 'r') as infile:
            content = infile.read()  
            print(f"Content of '{input_file}':\n{content}")
        
       
        with open(output_file, 'w') as outfile:
            outfile.write(content) 
            print(f"Content successfully written to '{output_file}'.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


input_file = "input.txt"
output_file = "output.txt"
read_and_write_file(input_file, output_file)
