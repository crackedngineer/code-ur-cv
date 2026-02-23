# Subhomoy Roy Choudhury Resume

## Local Setup

To build and compile the resume locally using Docker:

1. **Build the Docker image:**
    ```bash
    make docker-build
    ```

2. **Compile the LaTeX resume inside the container:**
    ```bash
    docker run --rm -v $(pwd):/workspace ghcr.io/youruser/latex-ci:latest make compile
    ```

> Ensure you have [Docker](https://www.docker.com/) and [Make](https://www.gnu.org/software/make/) installed on your system.

The compiled PDF will be available in your project directory.