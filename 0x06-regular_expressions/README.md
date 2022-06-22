## Regular expression

here is the Ruby code that I will use in this project

```ruby
sylvain@ubuntu$ cat example.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
sylvain@ubuntu$
sylvain@ubuntu$ ./example.rb 127.0.0.2
127.0.0.2
sylvain@ubuntu$ ./example.rb 127.0.0.1
127.0.0.1
sylvain@ubuntu$ ./example.rb 127.0.0.a
```

* our Bash scripts should be like this:
#!/usr/bin/env ruby

* my regex is built for the Oniguruma Library

```bash
Some people, when confronted with a problem, think
“I know, I'll use regular expressions.”   Now they have two problems.
```

# Made by Jebeniani Aymen @C17
