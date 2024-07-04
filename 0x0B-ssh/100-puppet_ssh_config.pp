# ssh config file
# SSH client configuration with puppet

ssh::client::host_config_entry { 'ubuntu':
    user                  => 'user',
    hostname              => 'ubuntu.example.com',
    identityfile          => '~/.ssh/school',
    passwordauthentication => 'no',
}

