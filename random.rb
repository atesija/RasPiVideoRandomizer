VIDEO_LOCATION =  "/media/pi/Windfish/Videos/**/*"
COMMERCIAL_LOCATION = '/media/pi/Windfish/Commercials/**/*'
BUMP_LOCATION = '/media/pi/Windfish/Bumps/**/*'
INTRO_LOCATION = '/media/pi/Windfish/Intros/**/*'

def get_videos_from_dir(directory)
    Dir[directory].select { |f| File.file? f }
end

all_videos = get_videos_from_dir(VIDEO_LOCATION)
commercial_videos = get_videos_from_dir(COMMERCIAL_LOCATION)
bump_videos = get_videos_from_dir(BUMP_LOCATION)
intro_videos = get_videos_from_dir(INTRO_LOCATION)

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

