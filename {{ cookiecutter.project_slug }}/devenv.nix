{ pkgs, lib, config, inputs, ... }:

{
  # https://devenv.sh/packages/
  packages = [ 
    pkgs.git

    {% if cookiecutter.k8s_enabled == 'y' %}
    # k8s
    pkgs.kubectl
    pkgs.kubernetes-helm
    pkgs.k3d  
    pkgs.dive
    pkgs.trivy
    {% endif %}

    # tools
    pkgs.gum
    pkgs.cookiecutter
    pkgs.go-task
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
