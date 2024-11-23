# Cookiecutter template for Devenv (Nix) + Taskfile + direnv projects

You can create a new project with

```bash
cookiecutter gh:gsantoro/project-template 
```

or alternatively if you don't have cookiecutter (and you don't want to install it)
but you have [uv](https://docs.astral.sh/uv/) already installed

```bash
uvx cookiecutter gh:gsantoro/project-template 
```

## Requirements
Once you have used cookiecutter to initialized your project, in order to work in the project you need to have:

- [devenv](https://devenv.sh/) installed.
- [direnv](https://direnv.net/docs/hook.html) configured to work with your terminal.


If you have [Task](https://github.com/go-task/task) installed already, you can install Devenv with 

```bash
task devenv:install
```

If you have brew installed already, you can install direnv with:

```bash
task direnv:install
```