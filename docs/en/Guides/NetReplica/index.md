# NetReplica - Configuration and Execution Guide in a Container

This guide describes the steps necessary to configure and run NetReplica in a Docker container, using Docker Compose. NetReplica is a tool dedicated to automating network laboratories through software.

## Prerequisites

- Docker installed on your machine: [Installation Instructions](https://docs.docker.com/get-docker/)
- Docker Compose installed on your machine: [Installation Instructions](https://docs.docker.com/compose/install/)

## Step 1: Environment Preparation

1. Open a terminal and clone the NetReplica repository using the following command:

```bash
git clone https://git.rnp.br/redes-abertas/netreplica-docker.git
```

2. Navigate to the cloned NetReplica directory:

```bash
cd netreplica-docker
```

## Step 2: Container Initialization

1. To build the Docker image and start the NetReplica container, run:

```bash
docker compose up -d
```

This command will create and start the container in the background.

## Step 3: Using NetReplica

After the container is initialized, you can interact with NetReplica using the commands below.

### Executing NetReplica

1. Place any necessary configuration files (`.conf` files) in the `conf` folder that is inside the `nrx` directory where the repository was cloned.

2. To run NetReplica with the `.conf` file, use the following command:

```bash
docker exec -it nrx nrx -c conf/<arquivo.conf>
```

- Replace `<arquivo.conf>` with the name of the configuration file you want to use.
- The output directory for the execution results is already specified inside the `.conf` file, so it is not necessary to specify it in the command.

### Alias for Agility

To further optimize the use of NetReplica, you can create an alias in your shell to simplify the execution command:

1. Open a terminal and edit the shell profile file corresponding to your system (for example, **`~/.bashrc`** for Bash or **`~/.zshrc`** for Zsh).
2. Add the following line to the end of the file:

```bash
alias nrx='docker exec -it nrx nrx'
```

3. Save the file and close it.
4. To activate the new alias without restarting the terminal, run the command:

```bash
source ~/.bashrc   # or source ~/.zshrc, depending on your shell
```

Now you can use the simplified command **`nrx`** to run NetReplica faster. For example:

```bash
nrx -c conf/<arquivo.conf>
```

### Monitoring Execution

- During execution, NetReplica will use the settings in the `.conf` file to access NetBox, start the replication and network analysis. Monitor the terminal output to track progress and view any relevant messages.
- After completion of execution, the replication and analysis results will be available in the output directory specified inside the `.conf` file.

### Shutting Down the Container

To shut down the NetReplica container and release resources, run:

```bash
docker compose down
```

## Next Steps: `.conf` File Configuration

Now that you know how to configure and run NetReplica,
the next step is to understand how to properly configure the `.conf` file to meet the needs of your network environment.

next steps [`.conf` File Configuration](NetReplica Guia Configuração e Execução com NetBox.md)