import turret.resolver as r

# res = r.uri_to_filepath("tank:/s125/maya_publish_shot_asset_cache_usd?Shot=vfx01_150&Sequence=vfx01&asset_type=fx&Asset=fxGrowthLadder&Step=fx&version=latest")
res = r.uri_to_filepath("tank:/s125/maya_publish_shot_asset_cache_usd?Step=animation&Task=animation&Shot=vfx01_160&version=latest&Sequence=vfx01&Asset=charHazmat02&AssetType=")
print("Final result:", res)