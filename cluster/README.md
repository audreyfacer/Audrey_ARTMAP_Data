# Cluster Files

This folder contains scripts and submission files for running experiments on the high-performance computing clusters.
The jobs are mainly `Slurm` submission scripts that simply run one or more of the experiment scripts in `src/experiments`.

## Useful Commands

### Interactive Jobs

#### `sinteractive`

This runs an interactive job with one node, many threads, and double the number of default memory per cpu:

```shell
sinteractive --time=12:00:00 --ntasks=32 --nodes=1 --mem-per-cpu=2000
```

This command does the same but on the CUDA nodes:

```shell
sinteractive cuda --time=12:00:00 --gres=gpu:1 --ntasks=32 --nodes=1 --mem-per-cpu=2000
```

#### `srun`

This works until if `sinteractive` is unavailable:

```shell
srun --time=12:00:00 --ntasks=32 --nodes=1 --mem-per-cpu=2000 --pty /bin/bash
```

With a GPU:

```shell
srun --time=12:00:00 --ntasks=32 --nodes=1 --mem-per-cpu=2000 --gres=gpu:1 --pty /bin/bash
```

### Slurm Commands

Show the Slurm config:

```sh
scontrol show config
```

Show specifically the priority parameters:

```sh
scontrol show config | grep Priority
```

Show the available partitions and their resources:

```sh
scontrol show partitions
```

### Anvil Commands

Interactive job:

```sh
sinteractive -p wholenode -N 2 -n 256 -A oneofyourallocations
```

For example:

```sh
sinteractive -p wholenode -N 2 -n 256 -A nairr240289-gpu
```
