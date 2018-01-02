input = gets
cww_idx = []
target = ['c', 'w', 'w']
ans = -1

input.each_char.each_with_index do |char, index|
  # when already 'c' found, overwrite index
  if char == 'c' && cww_idx.length > 0 then
    cww_idx = [index]
    next
  end

  cww_idx.push(index) if char == target[cww_idx.length]
  
  if cww_idx.length == 3 && (ans == -1 || ans > (cww_idx.last - cww_idx.first) + 1) then
    ans = (cww_idx.last - cww_idx.first) + 1
    cww_idx = []
  end
end

p(ans)
