VIDEO_LOCATION =  "/media/pi/Windfish/Videos/**/*"
all_videos = Dir[VIDEO_LOCATION].select { |f| File.file? f }

shows = ARGV
show_filenames = []
shows.each do |show|
    videos = all_videos.select{ |v| v.include? show }.sort
    show_filenames << videos
end

final_show_list = []
while !show_filenames.empty? do
    index = rand(0..(show_filenames.length - 1))
    final_show_list << show_filenames[index].shift unless show_filenames[index].empty?
    show_filenames.delete_at(index) if show_filenames[index].empty?
end

final_show_list.each do |show|
    puts "Playing: #{show}"
    `lxterminal -e omxplayer '#{show}' -b -o hdmi`
    sleep 1
    while `ps ax`.include?('omxplayer') do
        sleep 1
    end
end

