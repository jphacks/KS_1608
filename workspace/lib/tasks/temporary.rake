namespace :temporary do
  desc 'do python script'
  task :python => :environment do
    system("python #{Rails.root}/scripts/python.py")
  end
end