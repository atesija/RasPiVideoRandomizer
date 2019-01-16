VIDEO_LOCATION =  "/media/pi/Windfish/Videos/**/*"
COMMERCIAL_LOCATION = '/media/pi/Windfish/Commercials/**/*'
BUMP_LOCATION = '/media/pi/Windfish/Bumps/**/*'
INTRO_LOCATION = '/media/pi/Windfish/Intros/**/*'

all_videos = Dir[VIDEO_LOCATION].select { |f| File.file? f }
commercial_videos = Dir[COMMERCIAL_LOCATION].select { |f| File.file? f }
bump_videos = Dir[BUMP_LOCATION].select { |f| File.file? f }
intro_videos = Dir[INTRO_LOCATION].select { |f| File.file? f }

shows = ARGV
final_show_list = shows.empty? ? all_videos : []
shows.each do |show|
    videos = all_videos.select{ |v| v.include? show }.sort
    final_show_list += videos
end
final_show_list.shuffle!
interstitial_videos = commercial_videos + bump_videos
interstitial_videos.shuffle!
intro_videos.shuffle!

puts "Playing: #{intro_videos[0]}"
`lxterminal -e omxplayer '#{intro_videos[0]}' -b -o hdmi`
sleep 1
final_show_list.each do |show|
    while `ps ax`.include?('omxplayer') do
        sleep 1
    end
    puts "Playing: #{show}"
    `lxterminal -e omxplayer "#{show}" -b -o hdmi`
    sleep 1
    
    while `ps ax`.include?('omxplayer') do
    sleep 1
    end
    puts "Playing: #{interstitial_videos[0]}"
    `lxterminal -e omxplayer '#{interstitial_videos[0]}' -b -o hdmi`
    sleep 1
end

