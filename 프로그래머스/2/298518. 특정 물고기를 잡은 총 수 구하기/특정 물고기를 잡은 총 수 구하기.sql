SELECT count(*) FISH_COUNT
FROM fish_info a JOIN fish_name_info b ON a.fish_type = b.fish_type
WHERE b.fish_name IN ('BASS', 'SNAPPER')