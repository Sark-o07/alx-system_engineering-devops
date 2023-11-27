# 0x0B. SSH

## 0. Use a private key

### Mandatory

To connect to your server using SSH, ensure that you have a private key named `school` in the `~/.ssh/` directory. Then, use the appropriate `ssh` command to connect to your server.

### Requirements:

- Only use ssh single-character flags.
- You cannot use `-l`.
- You do not need to handle the case of a private key protected by a passphrase.

## 1. Create an SSH key pair

### Mandatory

To create an RSA key pair, follow the specified requirements without providing the actual script.

### Requirements:

- Name of the created private key must be `school`.
- Number of bits in the created key to be created is 4096.
- The created key must be protected by the passphrase `betty`.

## 2. Let me in!

### Mandatory

To allow us to connect to your server using the `ubuntu` user, add the provided SSH public key to the `~/.ssh/authorized_keys` file on your server.

Now, we should be able to join the party and connect to your server using the provided public key.
