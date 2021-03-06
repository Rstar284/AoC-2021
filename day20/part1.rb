alg, grid = File.open('input') do |f|
    alg = f.readline.chomp
    f.readline
    grid = f.readlines.map(&:chomp)
    [alg, grid]
end

def tick(alg, grid, flip)
    (-2..(grid.size+1)).map do |x|
      (-2..(grid[0].size+1)).map do |y|
        bits = []
        (-1..1).each do |dx|
          (-1..1).each do |dy|
            if (0...grid.size) === x + dx && (0...grid[0].size) === y + dy
              bits << (grid[x + dx][y + dy] == '#' ? 1 : 0)
            else
              bits << (flip ? 1 : 0)
            end
          end
        end
        index = bits.join.to_i(2)
        alg[index]
      end
    end
end

flip = false
2.times do
  grid = tick(alg, grid, flip)
  if alg[0] == '#'
    flip = !flip
  end
  puts grid.map(&:join).join("\n")
end
puts grid.map(&:join).join("\n")
p grid.flatten.count('#')