import os

def makeCommits(days : int):
    if days < 1:
        os.system('git push')
    else:
        dates = f"{days} days ago"
        with open('data.txt', 'a') as file:
            file.write(f'{dates} <- this was the commit for the day!!\n')
        os.system('git add data.txt')
        os.system(f'git commit --date="{dates}" -m "First commit for the day!"')
        return makeCommits(days - 1)

makeCommits(365)
