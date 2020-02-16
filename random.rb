VIDEO_LOCATION =  "/media/pi/Windfish/Videos/**/*"
COMMERCIAL_LOCATION = '/media/pi/Windfish/Commercials/**/*'
BUMP_LOCATION = '/media/pi/Windfish/Bumps/**/*'
INTRO_LOCATION = '/media/pi/Windfish/Intros/**/*'
COMMERCIALS_PER_VIDEO = 2

commercials = ARGV.include?('-c')
ARGV.delete('-c')

def get_videos_from_dir(directory)
    Dir[directory].select { |f| File.file? f }
end

all_videos = get_videos_from_dir(VIDEO_LOCATION)
commercial_videos = get_videos_from_dir(COMMERCIAL_LOCATION)
bump_videos = get_videos_from_dir(BUMP_LOCATION)
intro_videos = get_videos_from_dir(INTRO_LOCATION)

shows = ARGV
full_shows_list = shows.empty? ? all_videos : []
shows.each do |show|
    videos = all_videos.select{ |v| v.include? show }.sort
    full_shows_list += videos
end

full_shows_list.shuffle!
interstitial_videos = commercial_videos + bump_videos
interstitial_videos.shuffle!
intro_videos.shuffle!

final_video_list = []
if commercials
    final_video_list = full_shows_list.zip(interstitial_videos.each_slice(COMMERCIALS_PER_VIDEO).to_a).flatten.compact
    final_video_list.unshift(intro_videos[0]) if !intro_videos.empty?
else
    final_video_list = full_shows_list
end

final_video_list.each do |show|
    puts "Playing: #{show}"
    `lxterminal -e omxplayer "#{show}" -b -o hdmi`
    sleep 1
    
    while `ps ax`.include?('omxplayer') do
        sleep 1
    end
end
