# 0x0A Configuration Management

This directory contains Puppet manifests to perform specific configuration management tasks.

## Task 0: Create a file

### Objective

Using Puppet, create a file in /tmp with specific requirements.

### Requirements

- File path: `/tmp/school`
- File permission: `0744`
- File owner: `www-data`
- File group: `www-data`
- File content: `I love Puppet`

### Implementation

The Puppet manifest for this task is in the file `0-create_a_file.pp`. To apply the configuration, use the following command:

```bash
puppet apply 0-create_a_file.pp
```

## Task 1: Install a package

### Objective

Using Puppet, install Flask from pip3 with specific requirements.

### Requirements

- Install Flask
- Version must be `2.1.0`

### Implementation

The Puppet manifest for this task is in the file `1-install_a_package.pp`. To apply the configuration, use the following command:

```bash
puppet apply 1-install_a_package.pp
```

## Task 2: Execute a command

### Objective

Using Puppet, create a manifest that kills a process named `killmenow`.

### Requirements

- Must use the `exec` Puppet resource
- Must use `pkill`

### Implementation

The Puppet manifest for this task is in the file `2-execute_a_command.pp`. To apply the configuration, use the following command:

```bash
puppet apply 2-execute_a_command.pp
```

Example:

```bash
# Terminal #0 - starting my process
```

Note: Ensure that Puppet is properly installed on your system before applying these manifests.

For more information on Puppet, refer to [Puppet Documentation](https://puppet.com/docs/).
