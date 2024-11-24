import sys
import paramiko
sys.path.append('../plg_UBUNTU/')
from a00_items import *


def Ssh_into_server(server_ip, SSH_username, SSH_password):
    try:

        client = paramiko.client.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(server_ip.strip(), username=SSH_username.strip(), password=SSH_password.strip())

        log(server_ip, 'info', "=> Connected")
        return client

    except paramiko.AuthenticationException as authException:
        log(server_ip, 'error', "=> NOT connected : %s" % authException)

    except paramiko.SSHException as sshException:

        log(server_ip, 'error', "=> Unable to establish SSH connection: %s" % sshException)

    except paramiko.SFTPError as sftpException:

        log(server_ip, 'error', "=> Unable to establish STFP session: %s" % sftpException)

    except socket.timeout as timeout_error:

        log(server_ip, 'error', "=> Connection timed out: %s" % timeout_error)

    except paramiko.ssh_exception.NoValidConnectionsError as no_valid_error:

        log(server_ip, 'error', "=> Unable to connect: %s" % no_valid_error)

    except Exception as e:

        log(server_ip, 'error', f"=> Error executing command: {e}")

    return None


def SSH_into_server_transport(server_ip, SSH_username, SSH_password):
    try:
        transport = paramiko.Transport((server_ip, 22))
        transport.connect(username=SSH_username, password=SSH_password)
        log(server_ip, 'info', "=> Transport Connected")
        sftp = paramiko.SFTPClient.from_transport(transport)
        return sftp

    except paramiko.AuthenticationException as authException:

        log(server_ip, 'error', "=> NOT connected : %s" % authException)

    except paramiko.SSHException as sshException:

        log(server_ip, 'error', "=> Unable to establish SSH connection: %s" % sshException)

    except paramiko.SFTPError as sftpException:

        log(server_ip, 'error', "=> Unable to establish STFP session: %s" % sftpException)

    except socket.timeout as timeout_error:

        log(server_ip, 'error', "=> Connection timed out: %s" % timeout_error)

    except paramiko.ssh_exception.NoValidConnectionsError as no_valid_error:

        log(server_ip, 'error', "=> Unable to connect: %s" % no_valid_error)

    except Exception as e:

        log(server_ip, 'error', f"=> Error executing command: {e}")

    return None


def server_details(server):
    try:
        server_ip = server.get('server_ip', None)
        ssh_username = server.get('ssh_username', None)
        ssh_password = server.get('ssh_password', None)

        if server_ip and ssh_username and ssh_password:
            return server_ip.strip(), ssh_username.strip(), ssh_password.strip()
        else:
            return None
    except Exception as e:
        log2('error', f"An error occurred: {e}")

        return None



def ssh_exec(ssh_client, cmd, get_pty=False):
    """
    Uses information from server object and ssh client instance
    to execute and log a given command.
    """

    log2('info', f"$ {cmd}")
    if ssh_client:
        try:
            stdin, stdout, stderr = ssh_client.exec_command(cmd, get_pty)
            for line in stdout:
                log2('info', line.strip("\n"))

            for line in stderr:
                log2('error', line.strip("\n"))
            return stdin, stdout, stderr

        except Exception as e:
            log2('error', f"Error executing command: {e}")



def ssh_exec2(ssh_client, cmd, get_pty=False):
    """
    Uses information from server object and ssh client instance
    to execute and log a given command.
    """

    log2('info', f"$ {cmd}")
    if ssh_client:
        try:
            stdin, stdout, stderr = ssh_client.exec_command(cmd, get_pty)
            return stdin, stdout, stderr

        except Exception as e:
            log2('error', f"Error executing command: {e}")


def log(s, log_level, message: str, flush=False) -> None:
    formatted_message = f"[{s}] {message}"
    log_level = log_level.upper()
    if flush:
        logger.log(log_level, formatted_message)
    else:
        logger.opt(depth=1).log(log_level, formatted_message)


def log2(log_level, message: str) -> None:
    log_level = log_level.upper()
    logger.log(log_level, message)
