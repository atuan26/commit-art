from subprocess import run


def commit(date):
    command = f'git commit --allow-empty --allow-empty-message -m "" --date="{date}"'
    run(command, shell=True)