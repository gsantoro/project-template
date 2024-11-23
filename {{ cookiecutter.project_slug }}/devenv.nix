{ pkgs, lib, config, inputs, ... }:

{
  # https://devenv.sh/packages/
  packages = [ 
    pkgs.git
    pkgs.gum
  ];

  {% if cookiecutter.python_enabled == 'y' %}
  languages.python = {
    enable = true;
    package = pkgs.python{{ cookiecutter.python_version | replace('.', '') }};
    uv = {
      enable = true;
      sync.enable = true;
    };
    venv.enable = true;
  };
  {% endif %}
}
