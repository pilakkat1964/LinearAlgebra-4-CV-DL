source "https://rubygems.org"

gem "github-pages", "~> 231", group: :jekyll_plugins
gem "jekyll-include-cache", group: :jekyll_plugins

# Windows and JRuby does not include zoneinfo files, so bundle the tzinfo-data gem
# and associated library. See https://github.com/tzinfo/tzinfo-data#usage
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end

# Performance-booster for watching directories on Windows
gem "wdm", "~> 0.1.1", :platforms => [:mingw, :x64_mingw, :mswin]

# Lock `http_parser.rb` to `v0.6.x` on JRuby. Lock to `v0.8.x` on all other rubies
# See: https://github.com/ruby/http_parser.rb/issues/45
platforms :jruby do
  gem "http_parser.rb", "~> 0.6.0"
end
