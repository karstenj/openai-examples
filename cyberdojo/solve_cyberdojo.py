# %%
import os
import sys
import glob
import time
import openai

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY


def get_desc(problem_name):
    # get a formatted description of the puzzle
    filename = problem_name + '_desc.txt'
    if os.path.isfile(filename):
        with open(filename, "r") as f:
            return f.read()
    return ''


def get_func(problem_name):
    # get a formatted description of the puzzle
    filename = problem_name + '_func.txt'
    if os.path.isfile(filename):
        with open(filename, "r") as f:
            return f.read()
    return ''


def get_solution_code(problem_name, temperature):
    prompt = get_prompt(problem_name)
    prefix, suffix = prompt.split("[insert]")

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prefix,
        suffix=suffix,
        temperature=temperature,
        max_tokens=1024,
        top_p=1,
        best_of=20,
        frequency_penalty=0,
        presence_penalty=0
    )

    insert_code = response.choices[0].text
    return insert_code


def generate_solution(problem_name, temperature):
    # use the [insert] code to write the full solution function
    insert_code = get_solution_code(problem_name, temperature)

    full_function = get_func(problem_name)
    full_function = full_function.replace('[insert]', insert_code)

    return full_function


def get_prompt(problem_name):
    # build the full prompt for the openai api

    prompt = ""
    desc = get_desc(problem_name)
    prompt += desc
    func = get_func(problem_name)
    prompt += f"""
Here is a python function which solves this puzzle: 
```
{func}

```

"""

    return prompt


def run_function(problem_name, code):
    print(code)
    # add function to scope
    exec(code, globals())

    fn_name = f"solve_{problem_name}"
    for filename in glob.glob(f'./{problem_name}_input_*.txt'):
        with open(filename, "r") as f:
            input_data = f.read()
            output_data = globals()[fn_name](input_data)
            print(input_data)
            print(output_data)

    return True

def solve(problem_name):
    # main solve function, should work with any year, day and part
    print(f"Solving {problem_name}...")
    tries_left = 5
    success = False

    while tries_left > 0 and not success:
        try:
            temperature = 1 - tries_left / 5
            tries_left -= 1
            code = generate_solution(problem_name, temperature)
            success = run_function(problem_name, code)
            if success:
                # save code to cache
                with open(f"{problem_name}.py", "w") as f:
                    f.write(code)

        except Exception as e:
            print(e)
            time.sleep(10)


# %%
solve(sys.argv[1])
#solve("anagrams")
