import pHash
# import dHash

# https://github.com/polachok/py-phash

#
# hash1 = pHash.imagehash('file.1.jpg')
# hash2 = pHash.imagehash('file.2.jpg')
# hash3 = pHash.imagehash('diff_file.jpg')
# hash4 = pHash.imagehash('diff_file2.jpg')
# print 'Hamming distance: %d (%08x / %08x)' % (pHash.hamming_distance(hash1, hash2), hash1, hash2)
# print 'Hamming distance: %d (%08x / %08x)' % (pHash.hamming_distance(hash1, hash3), hash1, hash3)
# print 'Hamming distance: %d (%08x / %08x)' % (pHash.hamming_distance(hash1, hash4), hash1, hash4)
# #
# digest1 = pHash.image_digest('file.1.jpg', 1.0, 1.0, 180)
# digest2 = pHash.image_digest('file.2.jpg', 1.0, 1.0, 180)
# print 'Cross-correelation: (%d,%d)' % (pHash.crosscorr(digest1, digest2))
#
#



# logo_hash = pHash.imagehash('video_wp.png')
# logo1_hash = pHash.imagehash('logo1.jpg')
# logo2_hash = pHash.imagehash('logo2.jpg')
# logo3_hash = pHash.imagehash('logo3.jpg')
# logo4_hash = pHash.imagehash('logo4.jpg')
#
# print 'Hamming distance: %d (%08x / %08x)' % (pHash.hamming_distance(logo_hash, logo1_hash), logo_hash, logo1_hash)
# print 'Hamming distance: %d (%08x / %08x)' % (pHash.hamming_distance(logo_hash, logo2_hash), logo_hash, logo2_hash)
# print 'Hamming distance: %d (%08x / %08x)' % (pHash.hamming_distance(logo_hash, logo3_hash), logo_hash, logo3_hash)
# print 'Hamming distance: %d (%08x / %08x)' % (pHash.hamming_distance(logo_hash, logo4_hash), logo_hash, logo4_hash)
#
#
# print 'Hamming distance: %d (%08x / %08x)' % (pHash.hamming_distance(logo1_hash, logo3_hash), logo1_hash, logo3_hash)
#




o4n_hash = pHash.imagehash('frame_o4n_03.jpg')
wp_hash = pHash.imagehash('frame_wp_003.jpg')
wpc_hash = pHash.imagehash('frame_wpc_0003.jpg')
wpstar_hash = pHash.imagehash('frame_wpstar_000056.jpg')

print 'Hamming distance: %d (%08x / %08x)' % (pHash.hamming_distance(o4n_hash, wp_hash), o4n_hash, wp_hash)
print 'Hamming distance: %d (%08x / %08x)' % (pHash.hamming_distance(o4n_hash, wpc_hash), o4n_hash, wpc_hash)
print 'Hamming distance: %d (%08x / %08x)' % (pHash.hamming_distance(wp_hash, wpc_hash), wp_hash, wpc_hash)
print 'Hamming distance: %d (%08x / %08x)' % (pHash.hamming_distance(wpstar_hash, wpc_hash), wpstar_hash, wpc_hash)
