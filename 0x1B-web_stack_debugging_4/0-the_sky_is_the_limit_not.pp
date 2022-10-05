# fix
exec { 'fix':
  command => 'rm -f etc/default/nginx && sudo service nginx restart',
  path    => '/usr/local/bin/:/bin/',
}
