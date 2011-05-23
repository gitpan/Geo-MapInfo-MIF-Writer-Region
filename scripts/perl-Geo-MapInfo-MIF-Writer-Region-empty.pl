#!/user/bin/perl
use strict;
use warnings;
use Geo::MapInfo::MIF::Writer::Region;

=head1 NAME

perl-Geo-MapInfo-MIF-Writer-Region-empty.pl - Empty Geo::MapInfo::MIF::Writer::Region Exmaple

=cut

my $map=Geo::MapInfo::MIF::Writer::Region->new(basename=>"empty");
$map->save;
