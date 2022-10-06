# Limits of files for a holberton user
exec { 'fix':
command => "/bin/sed -i 's/holberton/none/g' /etc/security/limits.conf"
}
